from django.contrib import admin
from  .models import  Products
from .models import Orders,PetProfile
# Register your models here.
admin.site.register([Products,Orders,PetProfile])
