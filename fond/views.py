from django.shortcuts import render, redirect
from .models import Form
from .forms import FormForm

def index(request):
    form = Form.objects.order_by('summ')
    return render(request,'main/fond.html',{'form':form})

def create(request):
    error = ''
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fond')
        else:
            error = 'ERROR'
    form = FormForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request,'main/fondCF.html',data)