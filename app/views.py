from django.shortcuts import render

# Create your views here.
def sports(request):
    return render(request,'sports.html')