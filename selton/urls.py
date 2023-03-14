from django.urls import path
from selton.views import *
app_name='something'
urlpatterns=[
    path('selton/',selton,name='selton')
]