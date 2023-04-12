from django.contrib import admin
from django.urls import include, path
from .views import *


urlpatterns = [
    path("",login_view,name="login"),   
    path("register/",registro,name="registro"),   
    path('logout/',logout_view,name="Logout"), 
    #path('',VistaLoginRegistro.as_view(),name='autenticacion'),
]
