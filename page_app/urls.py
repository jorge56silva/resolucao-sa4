from django.urls import path
from page_app.views import index, contato, services

urlpatterns = [
    path('', index),
    path('services/', services),
    path('services/contato/', contato), 
    path('contato/', contato), 
]
