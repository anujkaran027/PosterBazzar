"""animebazzar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from animebazzar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about-us/', views.aboutus,name="about-us"),
    path('contact-us/', views.contactus),
    path('track-your-order/', views.trackorder),
    path('shop/', views.shop),
    path('terms-and-conditions/', views.TandC),
    path('return-and-refund/', views.RandR),
    path('privacy-policy/', views.privacy),
    path('sitemap/', views.sitemap),
    path('login/', views.loginpage),
    path('signup/', views.signuppage),
    path('logout/', views.logoutpage),
    path('shop/<itemid>', views.productpage, name='product_detail'),
    path('cart/', include('cart.urls')),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)