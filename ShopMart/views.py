from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    category = ['Clothes', 'Smartphones', 'Home Appliances', 'Shoes','Electronics Devices','Opticals', 'Personal Care', 'Jewelery & Acc', 'Stationary', 'Bags']
    params = {'category' : category}
    return render(request, 'index.html', params)
    #return HttpResponse("<h2>Hello Everyone, Welcome to the Shopping Mart. <br> Happy Shopping..! </h2>")

def about(request):
    return HttpResponse("<h1>This is a Shopping Mart.<br> Here you can buy multiple products with reasonable rates, best quality assured. </h1>") 

def contact(request):   
    return HttpResponse("<h1> Contact Us <br> email id : xyz@gmail.com <br>   Ph.No : 0562-2252098 </h1>")       