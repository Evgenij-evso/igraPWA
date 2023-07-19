
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('approval',views.approval,name='approval'),
    path('hpay',views.history_pay,name='history_pay'),
    path('acc',views.acc,name='acc'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search')
]
