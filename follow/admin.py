from django.contrib import admin

# Register your models here.
from follow.models import Calend
from follow.views import home

admin.site.register(Calend)
