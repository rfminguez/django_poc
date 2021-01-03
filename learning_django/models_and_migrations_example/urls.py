from django.urls import path
from . import views

app_name = "models_and_migrations_example"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
]
