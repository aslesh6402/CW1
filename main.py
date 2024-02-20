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

	# time showing in phone
	obj=TimezoneFinder()
	result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

	home=pytz.timezone(result)
	local_time=datetime.now(home)
	current_time=local_time.strftime("%I:%M:%p")
	clock.config(text=current_time)

# logo
logo=PhotoImage(file="Images/logoimage.png")
Label(root,image=logo).place(x=240,y=70)

Heading=Label(root,text="TRACK NUMBERS",font=("arial",15,"bold"))
Heading.place(x=84,y=110)

# Entry
Entry_back=PhotoImage(file="Images/search png.png")
Label(root,image=Entry_back).place(x=20,y=190)