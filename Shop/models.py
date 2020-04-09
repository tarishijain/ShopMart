from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 200)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.CharField(max_length = 50)
    #image_link = models.ImageField(width_field = 70, height_field = 50)
    created_at = models.DateTimeField()

    def __str__(self):
        return "%i : Name : %s Desc : %s Price : %i Discount : %i Category : %s Created At : %s" % (self.id,self.name,self.desc, self.price, self.discount, self.category, self.created_at)