from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),  # Home page route
    path('Order/', views.Order, name='Order'),
    path('About/', views.About, name='About'),
    path('Contactus/', views.Contactus, name='Contactus'),
    path('Services/', views.Services, name='Services'),
 
    

]