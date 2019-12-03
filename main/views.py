from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
import requests

# Create your views here.
def home(request):
    context = {

    }
    return render(request,'home.html',context)

def metroList(request):
    return render(request,'metrolist.html')

def metroapi(request):
    url = "/"
    if request.method == 'POST':
        fromStation = request.POST.get("fromField")
        toStation = request.POST.get("toField")
        fromStation = fromStation.strip()
        toStation = toStation.strip()
        url = "/metroapi/from={}&to={}".format(fromStation,toStation)
    return redirect(url)

def apiRedirect(request,fromStation,toStation):
    resp = {}
    fromArr = []
    toArr = []
    finalFrom = ''
    finalTo = ''
    fromStation = fromStation.strip().lower()
    toStation = toStation.strip().lower()
    fromArr = fromStation.split(" ")
    toArr = toStation.split(" ")
    for val in fromArr:
        if val != '':
            finalFrom += val.capitalize()
            finalFrom += " "

    for val in toArr:
        if val != '':
            finalTo += val.capitalize()
            finalTo += " "

    finalTo = finalTo.strip()
    finalFrom = finalFrom.strip()
    data = requests.get("https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from={}&to={}".format(finalFrom,finalTo))
    resp = json.loads(data.text)
    
    return JsonResponse(resp,safe=False)