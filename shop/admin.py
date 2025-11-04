from django.contrib import admin
from shop.models import product_categories
from shop.models import products

# Register your models here.

class admincategories(admin.ModelAdmin):
    list_display = ['category_name']

admin.site.register(product_categories,admincategories)


class adminproducts(admin.ModelAdmin):
    list_display =['name','discountprice','category']

admin.site.register(products,adminproducts)