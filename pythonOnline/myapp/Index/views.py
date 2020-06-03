from django.shortcuts import render
from .models import Post # import model

# Create your views here.
def Home(request):
    objList = Post.objects.all()
    return render(request,'home.html',{'objList':objList})
