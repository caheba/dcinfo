from django.contrib import admin

from .models import Change 
from .models import VServer

# Register your models here.

admin.site.register(Change)
admin.site.register(VServer)
