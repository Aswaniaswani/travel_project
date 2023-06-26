from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib import auth
from .models import Traveler,Contact,Career,Apply

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'index.html')
def regindex(request):
    return render(request, 'regindex.html')
def ruser(request):
    if request.method=="POST":
        uname=request.POST['un1']
        email=request.POST['e1']
        password=request.POST['p1']
        repassword = request.POST['rP1']
        if password==repassword:
            obj=Traveler.objects
        else:
            print("password not matching")
        obj=Traveler.objects.create(name=uname,email=email,password=password,re_password=repassword)
        obj.save()
        return redirect('/')
    return render(request,'logindex.html')
def logindex(request):
    return render(request, 'logindex.html')
def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(name=username,password=password)
        if user is not None:
            # auth.logindex(request,user)
            return redirect('/regindex')
        else:
            return redirect('/index')
    return render(request,'index.html')
def logout(request):
        auth.logout(request)
        return render('/')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def contactus(request):
    if request.method=="POST":
        name=request.POST['n2']
        email=request.POST['e2']
        subject=request.POST['s1']
        message= request.POST['ma1']
        obj = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        obj.save()
        # return redirect('/')
    return render(request, 'index.html')
def guide(request):
    return render(request, 'guide.html')
def service(request):
    return render(request, 'service.html')
def single(request):
    return render(request, 'single.html')
def career(request):
    return render(request,'career.html')
# def career(request):
#     details = Career.objects.all()
#     return render(request,'career.html',{'details':details})
def travelguide(request):
    details = Career.objects.all()
    return render(request,'travelguide.html',{'details':details})
def indexapply(request):
    return render(request, 'indexapply.html')
def appnow(request):
    if request.method=="POST":
        name=request.POST['na3']
        email=request.POST['em3']
        address=request.POST['ad3']
        cv=request.POST['cv']
        obj = Apply.objects.create(name=name, email=email, address=address,cv=cv)
        obj.save()
        return redirect('/career')
    return render(request, 'index.html')

