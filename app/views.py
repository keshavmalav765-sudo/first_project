from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,user
from news.models import news
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login
from django.views.generic import ListView

# Create your views here.

def home(request):
    if request.method=="GET":
        print("home page open ho gya ")
    else:
        print("mistek ho gyi bhai")
    return render (request,'home.html')

def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')


# def product_det(request):
#         search=request.GET.get("search")
#         if search:
#             products=product.objects.filter(name__icontains=search)
#         else:
#             products=product.objects.all().order_by("-name")
#         return render(request,"products.html",{
#             "products": products
#         })
class product_det(ListView):
    model=product
    template_name="products.html"
    context_object_name="products" 
    
    def get_queryset(self):
        search=self.request.GET.get("search")
        if search:
            return product.objects.filter(name__icontains=search)     
        return product.objects.all()

    
# def ragister_det(request):
#     if request.method=="POST":
#         u_name=request.POST.get("my_username") 
#         u_pass=request.POST.get("my_password")
#         if u_name and u_pass:
#             sec_pass=make_password(u_pass)
#             user.objects.create(username=u_name,password=sec_pass)
#             return HttpResponse('congratulation you are ragister')
#     return render(request,'ragister.html')


def user_det(request):
    if request.method=="POST":
        u_name=request.POST.get("username")
        u_pass=request.POST.get("password")
        u_email=request.POST.get("email")
        if u_name and u_email and u_pass:
            sec_pass=make_password(u_pass)
            user.objects.create(name=u_name,password=sec_pass,email=u_email)
            return HttpResponse('your are ragister')
    return render(request,'ragister.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from .models import user  # Aapka custom user model

def login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get("username")
        u_pass = request.POST.get("password")
        
        try:
            # Database mein check karein ki user exist karta hai ya nahi
            existing_user = user.objects.get(name=u_name)
            
            # Password verify karein (encrypted password ke sath match karna)
            if check_password(u_pass, existing_user.password):
                # Login successful! Session ya home page par redirect karein
                return HttpResponse(f'Welcome back, {existing_user.name}! Aap successfully login ho gaye hain.')
            else:
                return HttpResponse('Galat password! Dobara koshish karein.')
        except user.DoesNotExist:
            return HttpResponse('Yeh username registered nahi hai!')
            
    return render(request, 'login.html')
def news_des(request):
    des=news.objects.all()
    return render(request,"login.html",{"des":des})


        
    




