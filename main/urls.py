
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('acc',views.acc,name='acc'),
    path('approval',views.approval,name='approval'),
    path('hpay',views.history_pay,name='history_pay')
]
