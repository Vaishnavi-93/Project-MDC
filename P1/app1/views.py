from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app1/home.html')

def contact(request):
    return render(request, 'app1/basic.html', {'content':['Drop an email to vvalipe@unomaha.edu for any concerns']})
