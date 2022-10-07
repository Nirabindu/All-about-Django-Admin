from django.db import models

# Create your models here.



class Category(models.Model):
    cat_name = models.CharField(max_length = 100, verbose_name = 'Category Name')
    date_added = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
        ordering = ('-date_added',)
    
    def __str__(self) -> str:
        return self.cat_name
    
class SubCategory(models.Model):
    sub_cat_name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = ('Sub Category')
        verbose_name_plural = ('SubCategories')
        # ordering = ('-date_added',)
        
    def __str__(self) -> str:
        return self.sub_cat_name