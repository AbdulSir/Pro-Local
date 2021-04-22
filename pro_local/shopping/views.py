from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
# Create your views here.


def index(request):
    google_map_api_key = "AIzaSyATsUAiN8HGEmtdItkO3n5E74FEKAelw5o"
    origin = "H4N 3B6" #user postal code
    destination = "H4N 3K1" #Store postal code, taken from the shops model
    res = urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=H4N+3B6&destinations=H4N+3K1&key=AIzaSyATsUAiN8HGEmtdItkO3n5E74FEKAelw5o").read()
    data = json.loads(res.decode())
    #print(data["rows"][0]["elements"][0]["distance"])
    return HttpResponse(data["rows"][0]["elements"][0]["distance"]["text"])
