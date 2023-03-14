from django.shortcuts import render

# Create your views here.
def seltos(request):
    f={'car':'car:seltos','price':'price:10.69'}
    return render(request,'Sample1.html',context=f)