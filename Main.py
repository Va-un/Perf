
#-------------------------------------------------------------------------------------
#IMPORTS
import streamlit as st
from pygame import mixer
import serial
import os
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from PIL import Image
#------------------------------------------------------------------------------------
#Functions
mixer.init()
def mus(user_choice):
    if user_choice == 'Classic':
        selected_audio = 'Classic_Bollywood.mp3'
    elif user_choice == "Jazz":
        selected_audio = 'Jazz.mp3'
    elif user_choice == 'Hindi':
        selected_audio = 'Instrumental Hindi Songs.mp3'
    elif user_choice == 'International':
        selected_audio = 'International.mp3'
    else:
        selected_audio = user_choice
    return selected_audio


def get_music_list():
    list_of_music_files = os.listdir("Music")
    return list_of_music_files

# Define a function to start playing a music file
def start_playing_music(song_name: str):
    print("Starting to play music")
    mixer.init()
    mixer.music.load(f"Music/{mus(song_name)}")
    mixer.music.play()
    st.success(f'🎶Now Playing {song_name}')

def stop_playing_music():
    print("Stopping music")
    mixer.quit()


def start_perfume(perfume_name: str):
    try:
        ser = serial.Serial("/dev/ttyUSB0", 9600)
        ser.write(perfume_name.encode())
        ser.close()

    except:
        st.error('NO perfume found')



def stop_perfume():
    try:
        print("Stopping perfume")
        ser = serial.Serial("/dev/ttyUSB0", 9600)
        ser.write("off".encode())
        ser.close()

    except:
        pass

def Enable(perfume_name,song_name):
    start_perfume(perfume_name)
    start_playing_music(song_name)


def Disable():
    stop_perfume()
    stop_playing_music()

def day():

    today = datetime.date.today()
    day_of_week = today.weekday()
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = day_names[day_of_week]
    return day_name


#------------------------------------------------------------------------------------
#Connecting to DataBase



#----------------------------------------------------------------------------------------
#WebSpace

st.title("Room1")
image = Image.open("Apartment.jpg")
st.image(image)

today = datetime.date.today()
st.write(today)



st.subheader("OR")

col1, col2 = st.columns(2)
# Music player column
col1.subheader("Pick The Song")
song_name = col1.radio("Pick one", get_music_list())

col1.button("Start", on_click=lambda: start_playing_music(song_name))
col1.button("Stop", on_click=stop_playing_music)

# Perfume controller column
col2.subheader("Pick The Perfume")
perfume_name = col2.radio("Pick one", ["ca32ts", "d23ogs"])
col2.button("ON", on_click=lambda: start_perfume(perfume_name))
col2.button("OFF", on_click=stop_perfume)

#volume
vol = st.slider('Music Vol', 0, 100,1)
mixer.music.set_volume(vol/10)  # Set music volume to half
