from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import registrationform 
from django.contrib.auth.forms import AuthenticationForm
from .models import*
from django.utils import timezone
from .models import PostModel
from .serializers import*
from rest_framework import viewsets
from rest_framework .response import Response
from rest_framework .views import APIView
# Create your views here.

def RegistrationView(request):
    if(request.method=="POST"):
        form=registrationform(request.POST,request.FILES)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            cpassword=form.cleaned_data.get('cpassword')

            if(password!=cpassword):
                messages.error(request,'password dose not match please try agin')
            else:
                user=form.save(commit=False)
                user.set_password(password)
                user.save()
                messages.success(request,'Registration succssfully completed')
                return redirect(LoginView)
    else:
        form=registrationform()
    return render(request,'registration.html',{'form':form})


def LoginView(request):
    if(request.method=="POST"):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if(user is not None):
                login(request,user)
                request.session['userid']=user.id
                messages.success(request,f'now you are loged as {username}')
                return redirect(profile)
            else:
                messages.error(request,'invalid username or password')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})
            

# user profile
def profile(request):
    id1 = request.session['userid']
    db = User.objects.get(id=id1)

    x=PostModel.objects.all()

    return render(request,'profile.html',{'data':db,'x':x})


# update profile

def UpdateProfile(request):
    id1 = request.session['userid']
    db = User.objects.get(id=id1)
    if(request.method == "POST"):
        db.username = request.POST.get('username')
        db.email = request.POST.get('email')
        if(request.FILES.get('image == None')):
            db.save()
        else:
            db.image = request.FILES.get('image')
        return redirect(profile)
    return render(request,'update_profile.html',{'data':db})


# 2.Blog post managemnet

class PostView(viewsets.ViewSet):
    serializer_class = PostSerializer
    model = PostModel

    def create(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        
    def list(self,request):
        model = PostModel.objects.all()
        serializer = PostSerializer(model,many=True)
        return Response(serializer.data)
    
    def update(self,request,**kwargs):
        id = kwargs.get("pk")
        model = PostModel.objects.get(id=id)
        serializer = PostSerializer(data=request.data,instance=model)
        if serializer.is_valid():
            return Response(serializer.data)
        else:return Response(request,serializer.errors)

        
    def retrieve(self,request,**kwargs):
        id = kwargs.get("pk")
        model = PostModel.objects.get(id=id)
        serializer = PostSerializer(model)
        return Response(request,serializer.data,{'serializer':serializer})
    
    def destroy(self,request,**kwargs):
        id = kwargs.get("pk")
        model = PostModel(id=id)
        return Response(request,'msg : item deleted',{'model':model})
    

        
        


def HomeView(request):
    model = PostModel.objects.all()
    return render(request,'home.html',{'model':model})
    

    
    



