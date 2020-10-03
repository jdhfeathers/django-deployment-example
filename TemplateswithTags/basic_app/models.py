from django.db import models
from django.forms import ModelForm

# Create your models here.
class Form_reg(models.Model):
    name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email=models.EmailField(max_length=264,unique=True)
    text=models.TextField(max_length=268)

    def __str__(self):
        return self.name