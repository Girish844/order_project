from django.contrib import admin
from .models import *
from .models import Test,user,restaurants,architecture,Article,Sold
# Register your models here.

admin.site.register(Test)
admin.site.register(user)
admin.site.register(restaurants)
admin.site.register(architecture)
admin.site.register(Article)
admin.site.register(Sold)

