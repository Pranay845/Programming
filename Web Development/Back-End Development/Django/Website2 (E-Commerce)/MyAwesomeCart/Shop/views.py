from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


# Create your views here.

def index(request):
    AllProducts = []
    CategoryProducts = Product.objects.values('category', 'id')
    Categories = {item['category'] for item in CategoryProducts}
    for Category in Categories:
        Products = Product.objects.filter(category=Category)
        n = len(Products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        AllProducts.append([Products, range(1, nSlides), nSlides])

    Parameters = {'AllProducts': AllProducts}
    return render(request, 'Shop/Home.html', Parameters)


def searchMatch(query, item):
    if query in item.product_name or query in item.category:
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    AllProducts = []
    CategoryProducts = Product.objects.values('category', 'id')
    Categories = {item['category'] for item in CategoryProducts}
    for Category in Categories:
        prodtemp = Product.objects.filter(category=Category)
        Products = [item for item in prodtemp if searchMatch(query, item)]
        n = len(Products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(Products) != 0:
            AllProducts.append([Products, range(1, nSlides), nSlides])
    Parameters = {'AllProducts': AllProducts, "msg": ""}
    if len(AllProducts) == 0 or len(query) < 4:
        Parameters = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'Shop/Search.html', Parameters)


def about(request):
    return render(request, "Shop/About.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        description = request.POST.get('description', '')
        contacts = Contact(name=name, email=email, phone=phone, description=description)
        contacts.save()
    return render(request, 'Shop/Contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_description, 'time': item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json},
                                          default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception:
            return HttpResponse('{"status":"error"}')

    return render(request, 'Shop/Tracker.html')


def productview(request, myid):
    # Fetch the Products using the id
    Products = Product.objects.filter(id=myid)
    return render(request, "Shop/ProductView.html", {'Products': Products[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                      state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_description="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'Shop/Checkout.html', {'thank': thank, 'id': id})
    return render(request, 'Shop/Checkout.html')
