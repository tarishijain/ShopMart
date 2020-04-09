from django.http import HttpResponse
from .models import Product
# Create your views here.

def crud(request):
    prod = Product(
        name = 'Sunglasses', desc = 'UV rays protected', price = 1800, discount = 10, 
        category = 'Opticals', created_at = '2020-02-01'
    )
    prod.save()
    objs = Product.objects.all()
    for obj in objs:
        print(obj)

    return HttpResponse("Done")