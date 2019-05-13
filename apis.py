from flask import Flask, render_template, request
import requests

@app.route('/sl')
def sl():
    r = requests.get('http://api.sl.se/api2/realtimedeparturesV4.json?key=016287db39614ed1a91365891e96af11&siteid=9528&timewindow=30')
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

@app.route('/chuck')
def chuck():
    r = requests.get('http://api.icndb.com/jokes/random')
    json_obj = r.json()
    return json_obj['value']['joke']
