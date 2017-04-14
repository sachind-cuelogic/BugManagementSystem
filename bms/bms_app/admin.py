from django.contrib import admin
from .models import Product_type
from .models import ProductDetails
from .models import ProductUser
from .models import UserRole

admin.site.register(Product_type)
admin.site.register(ProductDetails)
admin.site.register(ProductUser)
admin.site.register(UserRole)
