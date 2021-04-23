from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
import urllib.request
import json
from shopping.models import *

# Create your views here.

def shop(request):
    # this takes care of generating all the information for the inventory view.
    context = {}
    if request.method == 'POST':
        #get the postal code from the post request
        postal = request.POST.get('postal')
        #if there's a space in the postal code, we clean it up
        if len(postal) == 7:
            postal = postal.replace(" ", "")
        #get the first character of the postal code
        location = postal[0]
        searched_item = request.POST.get('search')
        shops = Shop.objects.all()
        product_list = []
        matching_product_list=[]
        #Searching for the inventory of a nearby store based on the first 3 characters of the postal code
        for shop in shops:
            if location.lower() == shop.postal_code[0].lower():
                print(shop)
                #adjust the distance of this store according to the location of the client
                origin = postal #user postal code
                destination = shop.postal_code #Store postal code, taken from the shops model
                res = urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+origin+"&destinations="+destination+"&key=AIzaSyATsUAiN8HGEmtdItkO3n5E74FEKAelw5o").read()
                data = json.loads(res.decode())
                #Setting the shop distance with respect to the client's location
                shop.distance = data["rows"][0]["elements"][0]["distance"]["text"]
                shop.save()
                #Adding all the products this store has to product_list
                product = Product.objects.filter(s_FK=shop.pk).all()
                if product is not None:
                    for item in product:
                        product_list.append(item) 
        if len(product_list) > 0:
            for item in product_list:
                if searched_item.lower() in item.p_name.lower():
                    matching_product_list.append(item)
        if len(matching_product_list)==0:
            messages.info(request, 'Sorry, no results were found!')
            return render(request, 'shop.html', context=context) 
        context = {
            "products": matching_product_list
        }
    return render(request, 'shop.html', context=context) # render the view

def cart(request):
    # this takes care of generating all the information for the inventory view.
    return render(request, 'cart.html') # render the view

def about(request):
    # this takes care of generating all the information for the inventory view.
    return render(request, 'about.html') # render the view

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
