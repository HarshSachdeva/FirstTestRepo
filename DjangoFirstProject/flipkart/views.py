from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Items
from django.core.validators import validate_integer

def ecart(request):
    return render(request, 'postcode.html')


def register(request):
    if request.method == 'POST':
        postcode = request.POST['postcode']
        return render(request, 'register.html', {'postcode': postcode})
    else:
        return render(request, 'register.html')



def catalog(request):
    item1 = Items()
    item2 = Items()
    item3 = Items()
    item4 = Items()
    item5 = Items()
    item6 = Items()

    item1.itemId = 1
    item1.itemName = "Banana"
    item1.itemDesc = "Grower's Selection Loose Banana"
    item1.itemPrice = "1"
    item1.expiryDte = "20-May"

    item2.itemId = 2
    item2.itemName = "Milk"
    item2.itemDesc = "British Whole Milk 4 pt"
    item2.itemPrice = "3"
    item2.expiryDte = "22-May"

    item3.itemId = 3
    item3.itemName = "Cadbury Chocolate"
    item3.itemDesc = "Chocolate bar 4 pack"
    item3.itemPrice = "1"
    item3.expiryDte = "30-June"

    item4.itemId = 4
    item4.itemName = "Rice"
    item4.itemDesc = "Uncle Ben's Long Grain Microwave Rice"
    item4.itemPrice = "2"
    item4.expiryDte = "20-Dec"

    item5.itemId = 5
    item5.itemName = "Wine"
    item5.itemDesc = "Hardys Classic Cabernet Merlot"
    item5.itemPrice = "9"
    item5.expiryDte = "10-Dec"

    item6.itemId = 6
    item6.itemName = "Bread"
    item6.itemDesc = "Hovis seed sensation"
    item6.itemPrice = "1"
    item6.expiryDte = "29-Apr"

    itemlist = [item1, item2, item3, item4, item5, item6]
    if request.method == 'POST':
        print('====submitRegistration = post ======')
        mobile = request.POST['mobile']
        if len(mobile) < 10:
            messages.info(request,'Invalid mobile number')
            redirect('register')
        email = request.POST['email']
        address = request.POST['address']
        pwd = request.POST['pwd']
        return render(request, 'catalog.html', {'address': address, 'itemlist': itemlist})
    else:
        return render(request, 'catalog.html', {'itemlist': itemlist})
    #return redirect('/catalog' , {'address': address})
    #return render(request, 'catalog.html')


def review(request):
    item1 = Items()
    item2 = Items()
    item3 = Items()
    item4 = Items()
    item5 = Items()
    item6 = Items()

    item1.itemId = 1
    item1.itemName = "Banana"
    item1.itemDesc = "Grower's Selection Loose Banana"
    item1.itemPrice = "1"
    item1.expiryDte = "20-May"

    item2.itemId = 2
    item2.itemName = "Milk"
    item2.itemDesc = "British Whole Milk 4 pt"
    item2.itemPrice = "3"
    item2.expiryDte = "22-May"

    item3.itemId = 3
    item3.itemName = "Cadbury Chocolate"
    item3.itemDesc = "Chocolate bar 4 pack"
    item3.itemPrice = "1"
    item3.expiryDte = "30-June"

    item4.itemId = 4
    item4.itemName = "Rice"
    item4.itemDesc = "Uncle Ben's Long Grain Microwave Rice"
    item4.itemPrice = "2"
    item4.expiryDte = "20-Dec"

    item5.itemId = 5
    item5.itemName = "Wine"
    item5.itemDesc = "Hardys Classic Cabernet Merlot"
    item5.itemPrice = "9"
    item5.expiryDte = "10-Dec"

    item6.itemId = 6
    item6.itemName = "Bread"
    item6.itemDesc = "Hovis seed sensation"
    item6.itemPrice = "1"
    item6.expiryDte = "29-Apr"

    itemlist = [item1, item2, item3, item4, item5, item6]

    if request.method == 'POST':
        address = request.POST['address']
        print("===========post ==========",address)
        selectedRows = request.POST.getlist('selectedRows')
        listOfSelectedRow = []
        j=0
        total=0
        for i in selectedRows:
            j = int(i)
            selectedRow = itemlist[j-1]
            selectedRow.quantity = request.POST['quantity'+i]
            total+= float(selectedRow.itemPrice)*float(selectedRow.quantity)
            listOfSelectedRow.append(selectedRow)
        return render(request, 'review.html',{'listOfSelectedRow': listOfSelectedRow, 'total': total,'address': address } )
    else:
        print("===========get ==========")
        return render(request, 'review.html')

def thankyou(request):
    return render(request, 'thankyou.html')
