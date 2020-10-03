from django.forms import ModelForm
from basic_app.models import Form_reg

class Form_User(ModelForm):
    class Meta:
        model=Form_reg
        fields=['name','last_name','email','text']