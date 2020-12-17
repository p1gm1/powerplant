# Django
from django.urls import path

from powerplant.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_powerplant_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("<str:username>/powerplant/", view=user_powerplant_view, name="powerplant")
]
