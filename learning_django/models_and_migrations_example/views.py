from django.shortcuts import render
from models_and_migrations_example.models import Flight


# Create your views here.
def index(request):
    flights = Flight.objects.all()

    return render(request, "airline/index.html", {
        "flights": flights
    })


def flight(request, flight_id):
    # TO-DO: hay que controlar si el flight_id existe o no

    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers

    return render(request, "airline/flight.html", {
        "flight": flight,
        "passengers": passengers.all()
    })
