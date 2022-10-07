from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length = 100, null = True , help_text = "This is  the name os user")
    age = models.IntegerField(null = True)
    sex = models.CharField(max_length = 1 , null = True)
    address = models.CharField(max_length = 100, null  = True)
    email = models.EmailField(unique = True, null = True)
    phone = models.IntegerField(null = True)
    qualification = models.CharField(max_length = 100, null = True)
    
    
    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Testy'
    
    
    '''
    needed when we want to show data that is in another model that have relation with this model we can see these field also using property
    '''    
    # @property
    # def email(self):
    #     return "%s"%(self.email)
    
    
    
    def __str__(self) -> str:
        return self.name
    