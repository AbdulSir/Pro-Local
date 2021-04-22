from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
# Create your views here.


def mapsAPITest(request):
    google_map_api_key = "AIzaSyATsUAiN8HGEmtdItkO3n5E74FEKAelw5o"
    origin = "H4N+3B6" #user postal code
    destination = "H4N+3K1" #Store postal code, taken from the shops model
    res = urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+origin+"&destinations="+destination+"&key=AIzaSyATsUAiN8HGEmtdItkO3n5E74FEKAelw5o").read()
    data = json.loads(res.decode())
    #print(data["rows"][0]["elements"][0]["distance"])
    return HttpResponse(data["rows"][0]["elements"][0]["distance"]["text"])

def cart(request):
    # this takes care of generating all the information for the inventory view.
    context = {}
    if request.method == 'GET':
        context = {

        }
    return render(request, 'cart.html', context=context) # render the view

def about(request):
    # this takes care of generating all the information for the inventory view.
    context = {}
    if request.method == 'GET':
        context = {

        }
    return render(request, 'about.html', context=context) # render the view

def shop(request):
    # this takes care of generating all the information for the inventory view.
    context = {}
    if request.method == 'GET':
        context = {

        }
    return render(request, 'shop.html', context=context) # render the view

def stores(request):
    # this takes care of generating all the information for the inventory view.
    context = {}
    if request.method == 'GET':
        context = {

        }
    return render(request, 'stores.html', context=context) # render the view
