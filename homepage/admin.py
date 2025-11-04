from django.contrib import admin
from homepage.models import home_page_slider
from homepage.models import home_page_categories

# Register your models here.

class adminhomepage(admin.ModelAdmin):
    list_display = ['sliderimg_name','slider_image',]

admin.site.register(home_page_slider,adminhomepage)


class adminhomepagecategories(admin.ModelAdmin):
    list_display = ['category_name','categories_img',]

admin.site.register(home_page_categories,adminhomepagecategories)