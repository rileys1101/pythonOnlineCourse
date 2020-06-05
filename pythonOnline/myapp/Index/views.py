from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post,UserForm # import model
from .forms import DBFrom #form for boottest

# Create your views here.
def Home(request):
    objList = Post.objects.all()
    return render(request,'home.html',{'objList':objList})
def UserData(request):
    objList = UserForm.objects.all()
    return render(request,'dataCheck.html',{'objList':objList})
def BootTest(request):
    #here
    if(request.method == 'POST'):
        # name = request.POST['name']
        # address = request.POST['address']
        form = DBFrom(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.save()
            return redirect('userdata') # redirect
    return render(request,'boot.html')

