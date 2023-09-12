from django.urls import path
from .views import *

urlpatterns=[
    path('custhome',CustomerHomeView.as_view(),name='custhome'),
    path('pdetail/<int:id>',ProductDetailView.as_view(),name='pdet'),
    path('acart/<int:id>',addcart,name='acart'),
    path('cart',CartlistView.as_view(),name='cartlist'),
    path('rcart/<int:id>',removecart,name='rcart'),
    path('payment/<int:id>',Payment.as_view(),name='pay'),
    path('order',Orderlistview.as_view(),name='order'),
    path('olist/<int:id>',cancelorder,name='olist'),
   
   
]