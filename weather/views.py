from tkinter import Y
from urllib import request
from django.shortcuts import render

# Create your views here.
import urllib.request
import json
from datetime import date, datetime, timedelta

day = datetime.now()
day2 = datetime.now() + timedelta(1)
day3 = datetime.now() + timedelta(2)
day4 = datetime.now() + timedelta(3)
dates = day.strftime("%d %b %Y")
dayname = day.strftime('%A')
dayname2, dayname3, dayname4 = day2.strftime('%a'), day3.strftime('%a'), day4.strftime('%a')

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=4dae004195ba16631fb6a817b8452162&units=metric").read()
        source2 = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4dae004195ba16631fb6a817b8452162&units=metric").read()
        datalist = json.loads(source)
        datalist2 = json.loads(source2)
        data ={
            "description" : datalist['list'][0]['weather'][0]['description'],
            "temp" : datalist['list'][0]['main']['temp'],
            "humidity" : datalist['list'][0]['main']['humidity'],
            "pressure" : datalist['list'][0]['main']['pressure'],
            "speed" : datalist['list'][0]['wind']['speed'],
            "name" : city,
            "country" : datalist2['sys']['country'],
            "date" : dates,
            "day" : dayname,
            "day2" : dayname2,
            "day3" : dayname3,
            "day4" : dayname4,
            "temp2" : datalist['list'][1]['main']['temp'],
            "temp3" : datalist['list'][2]['main']['temp'],
            "temp4" : datalist['list'][3]['main']['temp'],
        }
    else:
        data = {}

    return render(request, 'index.html', data)