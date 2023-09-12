
from django.urls import path,include
from .views import *


urlpatterns=[ path('userreg',Userregview.as_view(),name='Ureg')]