from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'main/info.html')



def approval(request):
    return render(request,'main/approval.html')


def history_pay(request):
    return render(request,'main/history_pay.html')

@login_required
def profile_view(request):
    return render(request, 'main/acc.html')