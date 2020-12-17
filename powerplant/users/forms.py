# Django
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# utils
import numpy as np
import joblib
import os

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):

    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class UserPowerplantForm(forms.Form):
    """Powerplant form"""
    
    temperature = forms.FloatField(label="Temperature °c",
                                   min_value=1.81,
                                   max_value=37.11,
                                   widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                   'required': True}))

    pressure = forms.FloatField(label="Ambient Pressure mlbar",
                                min_value=992.89,
                                max_value=1033.30,
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'required': True}))
    
    humidity = forms.FloatField(label="Relative Humidity %",
                                min_value=25.56,
                                max_value=100.16,
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'required': True}))

    vacuum = forms.FloatField(label="Exhaust Vacuum cm Hg",
                              min_value=25.36,
                              max_value=81.56,
                              widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'required': True}))

    def save(self, request):
        user = User.objects.get(username=request.user.username)
        user.at = self.cleaned_data['temperature']
        user.ap = self.cleaned_data['pressure']
        user.rh = self.cleaned_data['humidity']
        user.v = self.cleaned_data['vacuum']
        n_energy = np.array([np.log1p(user.at), 
                             np.log1p(user.ap), 
                             np.log1p(user.rh), 
                             np.log1p(user.v)])
        model = joblib.load(os.path.dirname(os.path.abspath(__file__))+'/ml/models/best_model.pkl') #TODO: Fix load of model
        pred = model.predict(n_energy.reshape(-1, 1))
        user.ep = list(np.expm1(pred))[3]
        user.save()