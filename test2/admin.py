from django.contrib import admin
from .models import *
from django.contrib.admin import SimpleListFilter
# Register your models here.


class EmailFilter(SimpleListFilter):
    
    '''
    custom filter
    Human- readable title which will be displayed in the 
    right admin side bar just above the filter options
    '''
    title = 'Email Filter'
    
    '''
    Parameter  for the filter that will be used in the url query
    '''
    parameter_name = 'email'
    
    def lookups(self, request, model_admin):
        
        '''
        Return a list of tuples. The first element in each tuple is the 
        coded value for the option that will appear in the url query.The 
        second elements is the human readable option that appear in the right
        side bar 
        '''
        
        return(
            ('has_email','has_email'),
            ('no_email','no_email')
        )
    def queryset(self, request, queryset):
        
        '''
        we have to create two query for has_email
        and for no_email
        '''
        if not self.value():
            return queryset
        if self.value().lower() == 'has_email' :
            return queryset.exclude(email = '')
        if self.value().lower()  == 'no_email':
            return queryset.filter(email = '')
            

class Filter(admin.ModelAdmin):
    list_display = ("id","email")
    list_filter = ("date_added",EmailFilter)

admin.site.register(Test2, Filter)