from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':25,'b':30}
    return render(request,'a1_first.html',d)
def a1_second(request):
    g={'a':'36','b':26,'c':21}
    return render(request,'a1_second.html',g)

