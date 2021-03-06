# Django
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.views.generic.edit import FormView
# Forms
from powerplant.users.forms import UserPowerplantForm

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("home")


user_redirect_view = UserRedirectView.as_view()

class UserPowerplantView(LoginRequiredMixin, FormView):

    model = User
              
    form_class = UserPowerplantForm
    
    template_name="users/user_powerplant.html"

    def get_initial(self):
        initial={'temperature': User.objects.get(username=self.request.user.username).at,
                 'pressure': User.objects.get(username=self.request.user.username).ap,
                 'humidity': User.objects.get(username=self.request.user.username).rh,
                 'vacuum': User.objects.get(username=self.request.user.username).v,
                 'output': User.objects.get(username=self.request.user.username).ep}
        return initial

    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("users:powerplant", kwargs={"username": self.request.user.username})

user_powerplant_view = UserPowerplantView.as_view()