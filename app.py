import flask
from collections import namedtuple
from flask import Flask, render_template, session, redirect, url_for, flash, request,jsonify
from flask_bootstrap import Bootstrap
import json
import math
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from flask_wtf import Form
import urllib2
from wtforms import SubmitField
from wtforms.validators import Required
from reg import taxiFare

def Uber(startPos, endPos):
    ohome = startPos
    home = ohome.strip().replace(' ','+')
    oend = endPos
    end = oend.strip().replace(' ','+')
    l = [home,end]
    n = []
    points = []
    final = []

    ## Finds lat,lng for inputs
    for i in l:
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+i+'&key=AIzaSyCLB1YY4m9pkyHK58xgisQsgCK3cTQKMU0'
        req = urllib2.Request(url)
        res = urllib2.urlopen(req).read()
        data = json.loads(res)
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        n += [[lat,lng]]



    ## Generates lat,lng points around 2 radius.
    ## The circle is generated around the user inputed end destination
    r = [.002,.001]
    c = range(9)
    for i in r:
        for j in c:
            lat = n[1][0] + math.sin(math.pi*j/4)*i
            lng = n[1][1] + math.cos(math.pi*j/4)*i
            points += [[lat,lng]]



    ## Adds rows in the following form: [address, uber, time, price, distance, lat, lng]
    session = Session(server_token = "xKx_P-GltMKQkmjor3sPp4nf91JHHyw1NDqiBdfr")
    client = UberRidesClient(session)
    for i in points:
        response = client.get_price_estimates(
            start_latitude=n[0][0],
            start_longitude=n[0][1],
            end_latitude=i[0],
            end_longitude=i[1],
            seat_count=2
        )
        estimate = response.json.get('prices')
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(i[0])+','+str(i[1])+'&key=AIzaSyCLB1YY4m9pkyHK58xgisQsgCK3cTQKMU0'
        req = urllib2.Request(url)
        res = urllib2.urlopen(req).read()
        data = json.loads(res)
        final += [[str(data['results'][0]['formatted_address']),'Uber',estimate[0]['duration']/60,(estimate[0]['low_estimate']+estimate[0]['high_estimate'])/2,estimate[0]['distance'],i[0],i[1]]]

    ## Sorts the list by price
    final.sort(key=lambda x: x[3])


    ## Adds the user inputed destination to the sorted list
    response = client.get_price_estimates(
        start_latitude=n[0][0],
        start_longitude=n[0][1],
        end_latitude=n[1][0],
        end_longitude=n[1][1],
        seat_count=2
    )
    estimate = response.json.get('prices')
    ## Added to the begining of the list
    final.insert(0,[oend,'Uber',estimate[0]['duration']/60,(estimate[0]['low_estimate']+estimate[0]['high_estimate'])/2,estimate[0]['distance'],n[1][0],n[1][1]])
    outputRows = []
    for element in final[0:7]:
        outputRows.append(element)

    #Compute Taxi Fares and append node to list
    fareTaxi = taxiFare(n[0][1], n[0][0],n[1][1], n[1][0],estimate[0]['distance'])

    d = []
    d.append({"Address": oend, "Transportation":"Taxi", "Price":fareTaxi, "Time":estimate[0]['duration']/60, "Distance":estimate[0]['distance']})
    column_names = ["Address", "Transportation", "Time", "Price", "Distance", "Lat", "Lon"]

    #Return JSON Format to HTML to Update Table
    for element in outputRows:
        aDict = {}
        for index in range(len(element)):
            aDict[column_names[index]] = element[index]
        d.append(aDict)
    return d

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

@app.route('/table')
def table():
    rows = [[]]
    column_names = ["Time (mins)", "Price ($)", "Transportation", "Distance (mi)", "Address"]
    return render_template("index.html", table=table,
        columns=column_names, rows=rows)

#GET Method to obtain user inputs and pass onto Uber function
@app.route('/_add_numbers')
def add_numbers():
    ohome = request.args.get('a',type=str)
    oend = request.args.get('b',type=str)
    list2 = Uber(ohome,oend)
    return jsonify(result=list2)

if __name__ == '__main__':
    app.run(debug=True)
