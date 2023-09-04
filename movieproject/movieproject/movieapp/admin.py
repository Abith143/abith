from django.contrib import admin

# Register your models here.
from .models import movie
class movieAdmin(admin.ModelAdmin):
    list_display = ('name',"year",'des','image')
admin .site.register(movie,movieAdmin)
