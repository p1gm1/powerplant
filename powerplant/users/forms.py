from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
    #TODO: Finish form

    temperature = forms.FloatField(label=True,
                                   min_value=1.81,
                                   max_value=37.11,
                                   widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                   'label': 'temperature',
                                                                   'required': True}))

    pressure = forms.FloatField(label=True,
                                min_value=992.89,
                                max_value=1033.30,
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'label': 'Ambient Pressure',
                                                                'required': True}))
    
    humidity = forms.FloatField(label=True,
                                min_value=25.56,
                                max_value=100.16,
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'label': 'Relative Humidity',
                                                                'required': True}))

    vacuum = forms.FloatField(label=True,
                              min_value=25.36,
                              max_value=81.56,
                              widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'label': 'Exhaust Vacuum',
                                                              'required': True}))

    output = forms.FloatField(label=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'id': 'disabledInput',
                                                              'label': 'Energy output'}))