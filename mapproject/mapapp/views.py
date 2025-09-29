from django.shortcuts import render

def map(request):
    return render(request,'map.html')

def grt(request):
    return render(request,'grt.html')

def adm(request):
    return render(request,'adambakkam.html')

def pho(request):
    return render(request,'phoenix.html')

def pala(request):
    return render(request,'palamudhir.html')

def rmkv(request):
    return render(request,'rmkv.html')




# Create your views here.
