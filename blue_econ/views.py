from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'blue_econ/index.html')


def Activities(request):
    return render(request,'blue_econ/Activities.html')


def Library(request):
    return render(request,'blue_econ/Library.html')
