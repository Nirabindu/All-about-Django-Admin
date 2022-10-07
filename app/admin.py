from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)




class CategoryAdminArea(admin.AdminSite):
    '''
    diff admin site as per user and model
    '''
    site_header = 'Category Admin'
    site_title = "Category Administrator"
    
    index_title = "CategoryAdmin"

category_admin_site = CategoryAdminArea(name = 'CategoryAdmin')

category_admin_site.register(Category)


class SubCategoryAdminArea(admin.AdminSite):
    site_header = 'SubCategory Admin'


subcategory_admin_site = SubCategoryAdminArea(name = 'SubCategoryAdmin')

subcategory_admin_site.register(SubCategory)


# Some process of registering models to admin

# process 1:
# admin.site.register(modelname) 

# process 2

# class PostAdmin(admin.ModelAdmin):
#     fields = ['','']
# or => '__all__'
# then=>
# admin.site.register(Pots, PostAdmin)

# using decorator
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ['','']
    

# process 3:

# import django.apps

# models = django.apps.apps.get_models()
# # we can get all the models at once from any app
# print(models)

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         '''
#         some model are already register we have to avoid them
#         '''
#         pass
        
        
'''
unregister a model
admin.site.unregister(modelname)
'''