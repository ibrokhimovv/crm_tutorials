from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', leads_list),
    path('<pk>/', leads_detail),
]