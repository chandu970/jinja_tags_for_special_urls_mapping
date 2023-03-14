from django.urls import path
from seltos.views import *
app_name='nothing'
urlpatterns=[
    path('seltos/',seltos,name='seltos'),
]