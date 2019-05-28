# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests
from myAPIkeys import TheKeys


appSecretKey = 'asdada!1231231ASdsadasSAdkiy324'

def nasa():
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key={}'.format(TheKeys.nasa))
    theDict = {'explanation': r.json()['explanation'],
                'media_type': r.json()['media_type'],
                'title': r.json()['title'],
                'url': r.json()['url']
                }
    return theDict

class Debaser():
    def __init__(self):
        tempdate = time()
        toDay = tempdate['date']
        toDay = ''.join(e for e in toDay if e.isalnum())
        toDay3 = int(toDay) + 3
        r = requests.get('http://www.debaser.se/debaser/api/?version=2&method=getevents&venue=&from={}&to={}&format=json'.format(toDay, toDay))

        if r.text != "":
            self.event = r.json()[0]['Event']
            self.subhead = r.json()[0]['SubHead']
            self.description = r.json()[0]['Description']
            self.open = r.json()[0]['Open']
            self.admission = r.json()[0]['Admission']
            self.ticketURL = r.json()[0]['TicketUrl']
            self.imageURL = r.json()[0]['ImageUrl']
            self.eventURL = r.json()[0]['EventUrl']
        else:
            self.event = 'No event today.'
            self.subhead = 'No event today.'
            self.description = 'No event today.'
            self.open = 'No event today.'
            self.admission = 'No event today.'
            self.ticketURL = 'http://www.aik.se'
            self.imageURL = ''
            self.eventURL = 'http://www.aik.se'

class Weather():
    def __init__(self):
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Stockholm,se&appid={}'.format(TheKeys.weather))
        self.status = r.json()['weather'][0]['main']
        temp = r.json()['main']['temp']
        x = float(temp-272.15)
        temp = round(x,2)
        self.temp = str(temp) + '\N{DEGREE SIGN} C'
        self.ort = r.json()['name']

def time():
    r = requests.get('http://worldtimeapi.org/api/timezone/Europe/Stockholm.json')
    json_obj = r.json()['datetime']
    theTime = json_obj[11:19]
    theDate = json_obj[:10]
    theDict = {'time':theTime, 'date':theDate}
    return theDict

def sl():
    r = requests.get('http://api.sl.se/api2/realtimedeparturesV4.json?key={}&timewindow=30'.format(TheKeys.sl))
    json_obj1 = r.json()['ResponseData']['Trains'][0]
    json_obj2 = r.json()['ResponseData']['Trains'][1]
    resa1 = {
    "TrainNumber": json_obj1["LineNumber"],
    "From": json_obj1["StopAreaName"],
    "Destination": json_obj1["Destination"],
    "Departs": json_obj1["DisplayTime"]}
    resa2 = {
    "TrainNumber": json_obj2["LineNumber"],
    "From": json_obj2["StopAreaName"],
    "Destination": json_obj2["Destination"],
    "Departs": json_obj2["DisplayTime"]}
    listResa = [resa1, resa2]
    return listResa

def chuck():
    r = requests.get('http://api.icndb.com/jokes/random')
    json_obj = r.json()
    return json_obj['value']['joke']
