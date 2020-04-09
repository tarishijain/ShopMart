from django.http import HttpResponse
from .models import Products
# Create your views here.

def crud(request):
    prod = Products(
        name = 'Sunglasses', desc = 'UV rays protected', price = 1800, discount = 10, 
        category = 'Opticals', created_at = '2020-02-01'
    )
    prod.save()
    objs = Products.objects.all()
    for obj in objs:
        print(obj)

    return HttpResponse("Done")