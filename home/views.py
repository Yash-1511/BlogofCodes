from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import BadHeaderError, send_mail
from blog.models import Post
# Create your views here.
def index(request):
    allpost= Post.objects.all()[:4]
    context={'allpost':allpost}
    return render(request,'home/index.html',context)
def about(request):
    return render(request,'home/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['yourname']
        email=request.POST['youremail']
        phone=request.POST['yourphone']
        msg=request.POST['yourmsg']
        contact=Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
        messages.success(request,"Thank you ! For Contacting us. We will reach you soon!")
    return render(request,'home/contact.html')
def handlesignup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if not password==cpassword:
            messages.error(request,"Password and confirm password do not match")
            return redirect('index')
        if len(username) > 10: 
            messages.error(request,"Username must lower than 10 characters")
            return redirect('index')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect('index')
        if User.objects.filter(email=email).exists():
            messages.error(request,"email address already exists")
            return redirect('index')
        myuser= User.objects.create_user(username=username,email=email,password=password) 
        myuser.save()
        messages.success(request,"Your Account has been created. Now you can login.")
        return redirect('index')
def handlelogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            messages.info(request,"Welcome")
            return redirect('index')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('index')
def handlelogout(request):
    logout(request)
    print("logout")
    return redirect('index')
def search(request):
    query=request.GET['search']
    if len(query) > 78:
        allpost=Post.objects.none()
    else:
        allpost=Post.objects.filter(title__icontains=query)
    params={"allpost":allpost,'query':query}
    return render(request,"home/search.html",params)