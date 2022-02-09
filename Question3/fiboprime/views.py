from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return render(request,"fiboprime/index.html")

# def nvalue(request):
#     return render(request,"fiboprime/index.html")



def prime(request):
    if request.method == "POST":
        n = int(request.POST["nvalue"])
        start = 1
        li=[]
        # n=100
        for num in range(start, n+1):
                if(num>1):
                    for i in range(2,num):
                        if(num%i)==0:
                            break
                    else:
                        li.append(num)
        return HttpResponse(f"Prime Numbers: { li }")

def fibo(request):
    # n=10
    if request.method == "POST":
        n = int(request.POST["nvalue"])
        
        n1,n2=0,1
        li=[]
        count=0
        while count < n:
            li.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

        return HttpResponse(f" Fibonaaci Series: { li }")
