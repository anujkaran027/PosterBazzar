from django.db import models


# Create your models here.


class product_categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name    


class products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(product_categories,on_delete=models.CASCADE)
    originalprice = models.IntegerField(null=True,blank=True)
    discountprice = models.IntegerField(default=0)
    description = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to="products/",max_length=250,null=True,blank=True)
    video = models.ImageField(upload_to="products/",max_length=500,null=True,blank=True,)

    @staticmethod
    def getproduct_by_id(categoryid):
        if categoryid:
            return products.objects.filter(category=categoryid)
        else:
            return products.objects.all()



    @property
    def getdiscountedpercent(self):
        disc = self.originalprice
        discp = self.discountprice
        
        if disc is not None:
            finalprice = (disc - discp)
            dsper = int(finalprice/disc*100)
            dsper = str(dsper)+"% OFF"
            return dsper
        else:
            return ''
        
    @property
    def getoriginalprice(self):
        origp = self.originalprice

        if origp is not None:
            origp = "Rs "+str(origp)
            return origp
        else:
            return ''

    @property
    def getdiscountedprice(self):
        dsp = self.discountprice
        dsp = "Rs "+str(dsp)
        return dsp