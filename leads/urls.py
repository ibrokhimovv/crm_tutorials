from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', leads_list),
    path('<int:pk>/', leads_detail),
    path('create/', create_load),
]
