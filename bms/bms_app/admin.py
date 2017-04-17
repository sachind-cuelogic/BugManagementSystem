from django.contrib import admin
from .models import Product_type
from .models import ProductDetails
from .models import ProductUser
from .models import UserRole
from .models import BugType
from .models import BugStatus
from .models import Bug_Details	

admin.site.register(Product_type)
admin.site.register(ProductDetails)
admin.site.register(ProductUser)
admin.site.register(UserRole)
admin.site.register(BugType)
admin.site.register(BugStatus)
admin.site.register(Bug_Details)
