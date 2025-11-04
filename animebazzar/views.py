from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from homepage.models import home_page_slider,home_page_categories
from shop.models import product_categories,products


def homepage(request):
    slider_images = home_page_slider.objects.values_list('slider_image',flat=True)
    cate_images = home_page_categories.objects.values_list('categories_img',flat=True)

    data ={
        'slider_images':slider_images,
        'cate_images':cate_images,
        }
    if request.user.is_authenticated:
        data['fname'] = request.user.first_name
    return render(request,"homepage.html",data)


def aboutus(request):
    return render(request,"aboutus.html")


def contactus(request):
    return render(request,"contactus.html")


def trackorder(request):
    return render(request,"trackorder.html")


def shop(request):
    items = products.objects.all()
    categories = product_categories.objects.all()
    categoryid = request.GET.get('category')

    if categoryid:
        items= products.getproduct_by_id(categoryid)
    elif request.method=="GET":
        st=request.GET.get('query')
        if st!= None:
            items = products.objects.filter(name__icontains=st)
    else:
        items = products.objects.all()

    data ={
        'items' : items,
        'categories':categories
    }
    return render(request,"shop.html",data)


def TandC(request):
    return render(request,"TandC.html")


def RandR(request):
    return render(request,"RandR.html")


def privacy(request):
    return render(request,"privacy.html")


def sitemap(request):
    return render(request,"sitemap.html")


def loginpage(request):

    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['pass1']

        print(email,password)

        user = authenticate(request,username=email, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            slider_images = home_page_slider.objects.values_list('slider_image',flat=True)
            cate_images = home_page_categories.objects.values_list('categories_img',flat=True)

            data ={
                'slider_images':slider_images,
                'cate_images':cate_images,
                'fname':fname,
                }
            return redirect('/',data)
        else:
            messages.error(request,"Wrong email or Password")
            return redirect('/login/')

    return render(request,"loginpage.html")


def signuppage(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(email=email):
            messages.error(request,"Email is already registered!")
            return redirect('/signup/')
        
        if len(pass1)<8:
            messages.error(request,"Password is too short")
            return redirect('/signup/')
        
        if pass1 != pass2:
            messages.error(request,"Password does not match!")
            return redirect('/signup/')

        newuser = User.objects.create_user(username=email, email=email, password=pass1)
        newuser.first_name = fname
        newuser.last_name = lname

        newuser.save()

        messages.success(request,"Registered Successfully")

        return redirect('/login/')

    return render(request,"signuppage.html")


def logoutpage(request):
    logout(request)
    slider_images = home_page_slider.objects.values_list('slider_image',flat=True)
    cate_images = home_page_categories.objects.values_list('categories_img',flat=True)

    data ={
        'slider_images':slider_images,
        'cate_images':cate_images,
        }

    return redirect('/',data)


def productpage(request,itemid):
    product = products.objects.get(id=itemid)

    data ={
        "products":product
    }
    print(product)
    return render(request,"product.html",data)