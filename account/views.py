
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import View,FormView,CreateView
from .forms import *


from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login




# Create your views here.
# class HomeView(View):
#     def get(self,request):
#         forms=LoginForm()
#         return render(request,"home.html",{"form":forms})

class HomeView(FormView):
    template_name="home.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")   
            pswd=form_data.cleaned_data.get("password")   
            user=authenticate(request,username=us,password=pswd)
            if user :
                login(request,user)
                messages.success(request,'login successfully')
                return redirect('custhome')
            else:
                messages.error(request,"login failed")
                return redirect('home')
        return render(request,"home.html",{"form":form_data})
    

# class Userregview(View):
#     def get(self,request):
#         forms=RegForm
#         return render(request,'register.html',{"form":forms})
#     def post(self,request):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,'sign up successfully')
#             return redirect('home')
#         return redirect(request,"register.html",{"form":form_data})


class Userregview(CreateView):
    template_name='register.html'
    form_class=RegForm
    model=User
    success_url=reverse_lazy('home')


    def form_valid(self, form):
        messages.success(self.request,"Registration successfull")
        return super().form_valid(form)
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
