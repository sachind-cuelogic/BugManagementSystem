from django.contrib import admin
from .models import ProjectType
from .models import ProductDetails
from .models import ProductUser
from .models import UserRole
from .models import BugType
from .models import BugStatus
from .models import BugDetails	
from .models import Comments	


admin.site.register(ProjectType)
admin.site.register(ProductDetails)
admin.site.register(ProductUser)
admin.site.register(UserRole)
admin.site.register(BugType)
admin.site.register(BugStatus)
admin.site.register(BugDetails)
admin.site.register(Comments)
