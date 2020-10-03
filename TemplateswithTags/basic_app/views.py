from django.shortcuts import render
from .forms import Form_User
from basic_app.models import Form_reg
# Create your views here.
def index(request):
    d={'phrase':'Phrase of the web here!'}
    return render(request, 'basic_app/index.html', context=d)

def page1(request):
    return render(request,'basic_app/page1.html')


def another(request):
    return render(request,'basic_app/another.html')

def user(request):
    user=Form_User()
    if request.method =='POST':
        user=Form_User(request.POST)
        if user.is_valid():
            user.save(commit=True)
            return index(request)
        else:
            print('error')
    return render(request,'basic_app/register.html',context={'user':user})