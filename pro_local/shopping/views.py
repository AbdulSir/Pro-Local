from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from django.template import RequestContext
import urllib.request
import json
from .models import *

# Create your views here.

def shop(request):
    # this takes care of generating all the information for the inventory view.
    context = {}
    if request.method == 'POST':
        #get the postal code from the post request
        postal = request.POST.get('postal')
        if postal == "":
            postal = "H3H1L2"
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
    #iterate the cookies to find the store cookies
    context = {}
    print(request.COOKIES)
    print(type(request.COOKIES))
    for key in dict(request.COOKIES):
        value = request.COOKIES.get(key)
        #check if this is a cart cookie
        #PLCART-SNAME-PNAME
        if "PLCART" in key:
            keys = key.split("-:-")
            if len(keys)>=3:
                #at least 3 parts to the key, find me the store
                store = Shop.objects.filter(s_name=keys[1]).first()               
                #print("NEXT")
                #print(keys[1])
                #print(keys[2])
                if store is not None:
                    print(store)
                    product = Product.objects.filter(s_FK__s_name=keys[1]).filter(p_name=keys[2]).first()
                    if product is not None:
                        print(product)
                        #use the get function to create a new elelemnt if it can not be found
                        check = context.get("shops", None)
                        if check is None:
                            #set the context shops value
                            context["shops"] = {}
                        products = {}
                        name = keys[1]
                        total = 0
                        link = store.s_link
                        distance = store.distance
                        #probuct values
                        qty = int(value)
                        productPrice = product.price
                        productName = product.p_name
                        productLink = product.p_link
                        productValue = product.price*qty
                        productImg = product.img
                        #set the shop if it does not exist already
                        shop = context["shops"].get(name, {"products":products, "name":name, "total":total, "link":link, "distance":distance})
                        print(shop)
                        #update the shops stored total
                        shop["total"] = shop["total"]+productValue
                        shop["products"][name+"-"+productName] = {"qty":qty, "price":productPrice, "value":productValue, "img":product.img, "link":productLink}
                        print(shop)
                        context["shops"][name] = shop
    print(context)
    return render(request, 'cart.html', context=context) # render the view


def about(request):
    return render(request, 'about.html') # render the view

def stores(request):
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
