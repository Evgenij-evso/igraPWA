
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='fond'),
    path('create',views.create, name='createfond')
]
