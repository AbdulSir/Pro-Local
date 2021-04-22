from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from shopping.models import *

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
        queryDict = request.GET
        search = queryDict.get('search', None)
        if search is not None:
            found = Shop.objects.all()#TODO: Change this to a contains
            if found is not None:
                context = {
                    "search": found,  
                }
        else:
            return HttpResponseNotFound("No Products Found")
    return render(request, 'shop.html', context=context) # render the view

def stores(request):
    # this takes care of generating all the information for the inventory view.
    context = {}
    if request.method == 'GET':
        queryDict = request.GET
        store = queryDict.get('name', None)
        if store is not None:
            found = Shop.objects.filter(s_name=store).first()
            if found is not None:
                context = {
                    "name": found.s_name,  
                    "street": found.address, 
                    "city": found.city, 
                    "prov": found.province, 
                    "blurb": found.blurb, 
                    "postal": found.postal_code, 
                }
        else:
            return HttpResponseNotFound("No Store Found")
    return render(request, 'stores.html', context=context) # render the view
