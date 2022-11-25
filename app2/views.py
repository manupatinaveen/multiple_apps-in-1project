from django.shortcuts import render

# Create your views here.
def a2_first (request):
    f={'a':90,'b':70,'c':80}
    return render(request,'a2_first.html',f)
