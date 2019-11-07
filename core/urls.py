from django.urls import path
from .views import home, contacto, comprar, servicios
urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('servicios/', servicios, name="servicios"),
    path('comprar/', comprar, name="comprar")
]
