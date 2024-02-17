import os
from tkinter import*
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.iconbitmap('Images/logo_PI6_icon.ico')
root.geometry("365x584+200+100")
root.resizable(False,False)

def track():
	entry_number=entry.get()
	number=phonenumbers.parse(entry_number)
	# country
	locate=geocoder.description_for_number(number, 'en')
	country.config(text=locate)
	# operator 
	operator=carrier.name_for_number(number, 'en')
	sim.config(text=operator)
	# Phone Timezone
	time=timezone.time_zones_for_number(number)
	zone.config(text=time)
	# logitude and latitude 
	geolocator=Nominatim(user_agent="geoapiExercises")
	location=geolocator.geocode(locate)

	lng=location.longitude
	lat=location.latitude
	longitude.config(text=lng)
	latitude.config(text=lat)
