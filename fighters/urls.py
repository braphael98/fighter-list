from django.urls import path
from fighters.views import index

urlpatterns = [
    path('', index)
]