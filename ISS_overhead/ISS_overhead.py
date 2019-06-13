#!/bin/python3

import json
import time
import turtle
import urllib.request

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# Lawrenceburg, IN
lat =  39.103993
lon = 84.512311
location = turtle.Turtle()
location.penup()
location.color('red')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' +str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

