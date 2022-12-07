from ast import operator
from re import search
from time import time
from tkinter import *
from turtle import heading
from unittest import result
import webbrowser
import folium
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
#############################     SIZE     ##############################
root=Tk()
root.title("Mobile Tracker (Sunny Sharma)")
root.geometry("365x584")
root.resizable(False,False)



##################   all   task    ###################################
def Track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)

#country
    locate=geocoder.description_for_number(number,'en')
    country.config(text=f"COUNTRY : {locate}")

    #operator
    operator=carrier.name_for_number(number,'en')
    sim.config(text=f"SIM : {operator}")

    #timezone
    time=timezone.time_zones_for_number(number)
    zone.config(text=f"ZONE : {time}")

   # longitude and latitude

    geolocator= Nominatim(user_agent="geospiExercises")
    location= geolocator.geocode(locate)
    lng=location.longitude
    lat=location.latitude
    longitude.config(text=f"LONGITUDE : {lng}")
    latitude.config(text=f"LATITUDE : {lat}")

    #time show
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")

    clock.config(text=f"CLOCK : {current_time}")






    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("location.html") 
    webbrowser.open('location.html') 




######################     all    task   end   ##########################




######  icon-image  #########
icon=PhotoImage(file="Tracking-Icon.png")
root.iconphoto(False,icon)

########  logo  ##########
logo=PhotoImage(file="xyz.png")
Label(root,image=logo).place(x=220,y=10)


########### search bar  ########
Eback=PhotoImage(file="sea1.png")
Label(root,image=Eback).place(x=5,y=190)


#######  heading  ###############
Heading=Label(root,text='TRACK NUMBER',font=('arial',15,'bold'))
Heading.place(x=70,y=90)


#########  bottom   #################
bm=PhotoImage(file="bg.png")
Label(root,image=bm).place(x=-2,y=332)


#########  ENTRY  ###################
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=('arial',20))
enter_number.place(x=30,y=200)


#########  bottom   #################
search_image=PhotoImage(file="th.png")
search=Button(root,image=search_image,borderwidth=0,cursor="hand2",bd=0,command=Track)
search.place(x=30,y=260)


#############  LABEL  (INFO.)  ###############
country=Label(root,text="COUNTRY : ",bg="#6600cc",fg="black",font=("arial",10,'bold'))
country.place(x=30,y=350)

sim=Label(root,text="SIM : ",bg="#6600cc",fg="black",font=("arial",10,'bold'))
sim.place(x=200,y=350)

zone=Label(root,text="ZONE : ",bg="#6600cc",fg="black",font=("arial",10,'bold'))
zone.place(x=30,y=400)

clock=Label(root,text="CLOCK : ",bg="#6600cc",fg="black",font=("arial",10,'bold'))
clock.place(x=30,y=450)

longitude=Label(root,text="LONGITUDE : ",bg="#6600cc",fg="black",font=("arial",10,'bold'))
longitude.place(x=30,y=500)

latitude=Label(root,text="LATITUDE : ",bg="#6600cc",fg="black",font=("arial",10,'bold'))
latitude.place(x=30,y=550)


root.mainloop()