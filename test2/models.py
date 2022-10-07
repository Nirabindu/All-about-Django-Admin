from django.db import models

# Create your models here.


class Test2(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    address = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = 'Test2'
        verbose_name_plural = 'Tests2'
        ordering = ('-date_added',)
    
    def __str__(self) -> str:
        return self.name