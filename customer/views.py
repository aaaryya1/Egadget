from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,View,DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from account.models import Product,Cart,Order
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.


def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"login first")
            return redirect("home")
    return inner
desc=[never_cache,signin_required]
# class CustomerHomeView(ListView):
#     def get(self,request):
#         res=Product.objects.all()
#         return render(request,"cust_home.html",{"data":res})

@method_decorator(desc,name='dispatch')
class CustomerHomeView(ListView):
    template_name="cust_home.html"
    queryset= Product.objects.all()
    context_object_name="products"

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('home')





# class ProductDetailView(View):
#     def get(self,request,**kwargs):
#         pid=kwargs.get('id')
#         pro=Product.objects.get(id=pid)
#         return render(request,"product_details.html",{"data":pro})
    

@method_decorator(desc,name='dispatch')
class ProductDetailView(DetailView):
    template_name="product_details.html"
    pk_url_kwarg='id'
    queryset=Product.objects.all()
    context_object_name='data'
@signin_required
def addcart(request,*args,**kwargs):
    id=kwargs.get("id")
    pro=Product.objects.get(id=id)
    user=request.user
    qty=request.POST.get('qnt')
    Cart.objects.create(Product=pro,user=user,quantity=qty)
    messages.success(request,"added to cart")
    return redirect('custhome')

@method_decorator(desc,name='dispatch')
class CartlistView(ListView):
    template_name="cart.html"
    queryset=Cart.objects.all()
    context_object_name="cart"
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
@signin_required   
def removecart(request,**kwargs):
    pid=kwargs.get("id")
    c=Cart.objects.get(id=pid)
    c.delete()
    messages.success(request,"Cart Item Removed")
    return redirect('cartlist')
@method_decorator(desc,name='dispatch')
class Payment(TemplateView):

    template_name="payment.html"

    def post(self,request,*args,**kwargs):
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        ad=request.POST.get("address")
        ph=request.POST.get("phone")
        Order.objects.create(cart=cart,address=ad,phone=ph)
        cart.status="order placed"
        cart.save()
        messages.success(request,"order placed successfully")
        return redirect("cartlist")
    

@method_decorator(desc,name='dispatch')
class Orderlistview(ListView):
    template_name="orders.html"
    queryset=Order.objects.all()
    context_object_name="order"


    def get_queryset(self):
        return Order.objects.filter(cart__user=self.request.user)
    

@signin_required
def cancelorder(request,*args,**kwargs):
    oid=kwargs.get("id")
    order=Order.objects.get(id=oid)
    order.status='cancelled'
    order.save()
    messages.success(request,"Order Cancelled")
    return redirect('order')  