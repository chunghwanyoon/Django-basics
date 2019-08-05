from django.contrib import admin

# relative import 현재 같은 디렉토리 안에 있기 때문에 .models를 사용함
from .models import Product


# Register your models here.
admin.site.register(Product)
