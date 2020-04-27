from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Items
from django.core.validators import validate_integer

def ecart(request):
    return render(request, 'postcode.html')


def signup(request):
    return render(request, 'register.html')


def register(request):
    mobile = request.POST['mobile']
    if len(mobile) < 10:
        messages.info(request,'Invalid mobile number')
        redirect('signup')
    email = request.POST['email']
    address = request.POST['address']
    pwd = request.POST['pwd']
    return render(request, 'catalog.html')


def catalog(request):

    if request.method == 'POST':
        selectedRows = request.POST.getlist('selectedRows')
        itemlist = request.POST.getlist('itemlist')
        print(selectedRows)
        print(itemlist[0])
        return render(request, 'review.html')
    else:
        item1 = Items()
        item2 = Items()
        item3 = Items()
        item4 = Items()
        item5 = Items()
        item6 = Items()

        item1.itemId = 1
        item1.itemName = "Banana"
        item1.itemDesc = "Grower's Selection Loose Banana"
        item1.itemPrice = "8.04 p/kg"
        item1.expiryDte = "30-Apr"

        item2.itemId = 2
        item2.itemName = "Milk"
        item2.itemDesc = "British Whole Milk 4 pt"
        item2.itemPrice = "£1.10"
        item2.expiryDte = "04-May"

        item3.itemId = 3
        item3.itemName = "Cadbury Chocolate"
        item3.itemDesc = "Chocolate bar 4 pack"
        item3.itemPrice = "£1"
        item3.expiryDte = "10-May"

        item4.itemId = 4
        item4.itemName = "Rice"
        item4.itemDesc = "Uncle Ben's Long Grain Microwave Rice"
        item4.itemPrice = "£2"
        item4.expiryDte = "25-June"

        item5.itemId = 5
        item5.itemName = "Wine"
        item5.itemDesc = "Hardys Classic Cabernet Merlot"
        item5.itemPrice = "£8.50"
        item5.expiryDte = "24-Dec"

        item6.itemId = 6
        item6.itemName = "Bread"
        item6.itemDesc = "Hovis seed sensation"
        item6.itemPrice = "£0.84"
        item6.expiryDte = "29-Apr"

        itemlist = [item1, item2, item3, item4, item5, item6]

        return render(request, 'catalog.html', {'itemlist': itemlist})


def review(request):
    return render(request, 'review.html', {'user': "review page"})


def thankyou(request):
    return render(request, 'thankyou.html', {'user': "thankyou page"})
