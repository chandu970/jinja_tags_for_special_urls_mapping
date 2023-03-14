from django.shortcuts import render

# Create your views here.
def selton(request):
    D={'car':'selton','price':'7.69'}
    return render(request,'Sample1.html',context=D)