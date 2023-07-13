
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('approval',views.approval,name='approval'),
    path('hpay',views.history_pay,name='history_pay'),
]
