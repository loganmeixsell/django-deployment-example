from django.urls import path, include
# Is the same as below from . import views
from basic_app import views

#This is for template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]