from django.http import HttpResponse
from django.shortcuts import render

def edad(request, edad):
    anio_nac = 2022 - edad
    return render(request,"home.html",{"anioNac":anio_nac})