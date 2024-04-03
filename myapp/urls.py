from django.urls import path
from myapp import views 

urlpatterns = [
path( "shop/" , views.index, name = "index" ),
path( "shop/contacto/" , views.contacto, name = "contacto" )
]