from django.shortcuts import render

def index(request):
    return render(request,'main/info.html')

def acc(request):
    return render(request,'main/acc.html')

def approval(request):
    return render(request,'main/approval.html')


def history_pay(request):
    return render(request,'main/history_pay.html')