from django.shortcuts import render
from account.models import Account
from blog.models import BlogPost


# Create your views here.
def home_screen_view(request):
    context = {}
    
    accounts = Account.objects.all()
    blogs = BlogPost.objects.all()
     
    context['accounts'] = accounts
    context['blogs'] = blogs
    
    return render(request, 'personal/home.html', context)