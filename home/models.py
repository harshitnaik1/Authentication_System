from django.db import models
# Create your models here.
class Employee(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=50, null=True)
    pass2 = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)