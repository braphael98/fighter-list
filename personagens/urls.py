from django.urls import path
from personagens.views import index

urlpatterns = [
    path('', index)
]