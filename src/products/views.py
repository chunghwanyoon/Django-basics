from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product
from .forms import ProductForm

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")  # string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>This is Contact page</h1>")
    return render(request, "contact.html", {})
 

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 45, 312, 289579]
    }
    return render(request, "about.html", my_context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = { 
        "form": form
        }   
    return render(request, "products/product_create.html", context)