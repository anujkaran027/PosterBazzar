from django.db import models

# Create your models here.

class home_page_slider(models.Model):
    sliderimg_name = models.CharField(max_length=20,default='test')
    slider_image = models.FileField(upload_to="homepage/",max_length=250,null=True,default=None)


class home_page_categories(models.Model):
    category_name = models.CharField(max_length=20,default='test')
    categories_img = models.FileField(upload_to="homepage_categories/",max_length=250,null=True,default=None)