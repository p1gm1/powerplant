# Django
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, FloatField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for powerplant."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    at = FloatField(default=25.00)
    v = FloatField(default=50.00)
    ap = FloatField(default=1000.00)
    rh = FloatField(default=50.00)
    ep = FloatField(default=0.00)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        context = {
            'username': self.username,
            'temperature': self.at,
            'exhaust_vacuum': self.v,
            'relative_humidity': self.rh,
            'ambient_pressure': self.ap,
            'electrical_energy':self.ep
        }
        return reverse("users:detail", **context)
