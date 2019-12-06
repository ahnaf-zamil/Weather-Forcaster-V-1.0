import requests
import math
from sys import stdin
from os import system

"""
Author: K.M Ahnaf Zamil
Written in Python 3
Github: ahnaf-zamil

"""

while (True):
	print("		Weather Forcasting app\n")
	print("	  	Made by K.M Ahnaf Zamil\n")
	city = input("  Enter the name of a city: ")
	print("")
	api_url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=2589ab45f6d805e48ae3deee8224bdc7'

	json_data= requests.get(api_url).json()
	lati = json_data["coord"]["lat"]
	long = json_data["coord"]["lon"]
	weath = json_data["weather"][0]["main"]
	weath_d=json_data["weather"][0]["description"]
	tempk= math.									floor(float(json_data["main"]["temp"]))
	tempf = math.floor((tempk-273.15)*1.8 + 32)
	tempc = math.floor(tempk-273.15)
	wind_speed=json_data["wind"]["speed"]
	wind_degree=json_data["wind"]["deg"]
	name= json_data["name"]
	country = json_data["sys"]["country"]


	print("  City: " + name)
	print("  Country: " + country)
	print("  Latitude: " + str(lati))
	print("  Longtitude: " + str(long))
	print("  Weather: " + weath)
	print("  Weather Description: " + weath_d)
	print("  Temperature: " +str(tempc)+" degrees Celsius")
	print("               " + str(tempf)+" degrees Farenheit")
	print("	       " +str(tempk) +" degrees Kelvin")
	print("  Wind Speed: " + str(wind_speed)+" meters per second at "+ str(wind_degree)+ " degrees")
	stdin.read(1)
	system("clear")

