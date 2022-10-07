from django.contrib import admin
from .models import *

# Register your models here.


TEXT = 'Puts User Information Here'

class TestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age","sex","address","email","phone",'qualification')
    list_filter = ['email','name']
    fieldsets  = (
        ('Personal Information',{
            'fields':('name','age','sex'),
            'description': '%s' % TEXT,
        }),
        ('Contact information',{
            'fields':('address','email','phone')
        }),
        ('Education',{
            'fields':('qualification',),
            'classes':('collapse',),
            
        }),
    )


admin.site.register(Test, TestAdmin)