from django.contrib import admin
from .models import User_info
from .models import Product_type
from .models import ProductDetails
from .models import ProductUser

admin.site.register(User_info)
admin.site.register(Product_type)
admin.site.register(ProductDetails)
admin.site.register(ProductUser)
