from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Bus
# from .forms import Bus_form
# Create your views here.
def main(request):
    return render(request,'bus_info/index.html')

def display(request):
    form=Bus.objects.all()
    return render(request,'bus_info/display.html',context={'form':form})