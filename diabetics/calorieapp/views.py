from django.shortcuts import render
from .models import Calorie
from .forms import Calorie_form
# Create your views here.
def calorieinfo(request):
    form=Calorie_form()
    if(request.method == 'POST'):
        form=Calorie_form(request.POST)
        if form.is_valid():
            form.save()

    return render(request,"calorieapp/index.html",context={'form':form})

def result(request):
    eatables=Calorie.objects.all()
    s=0
    for i in eatables:
        s+=i.calorie
    print(eatables)
    return render(request,"calorieapp/result.html",{
        
        "eatables":eatables,"total":s
    })