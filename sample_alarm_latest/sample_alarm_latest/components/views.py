from django.shortcuts import render
from django.utils import timezone
import logging
import os
import signal
import asyncio
import datetime
import threading
import subprocess
from apscheduler.schedulers.background import BackgroundScheduler

from gpiozero import LED
from time import sleep
import pygame
import os
import random

from sample_alarm_latest.components.models import Timer
from tuya.devices import TuyaSmartSwitch

device = TuyaSmartSwitch(username="er.madhav21@gmail.com", password="Password1314", location="EU", device="014033082cf4323237a7")


led = LED(14)

led.off()

songs_collection = []

songs_path = "/home/pi/Documents/Git_RPI_Project/RPI_4/sample_alarm_latest/songs/"

def test_view(request):
    blocks = {'name': 'Kali :*'}
    
    pygame.mixer.init()
    
    if request.method == 'POST':

        if 'set' in request.POST:

            timer_data = set_alarm(request)

            # Call background scheduler
            call_scheduler(request, timer_data)

            blocks = {'stop_button': 'true', 'message': 'Alarm Set', 'time': timer_data}

            return store_time(request, blocks)

        # Else if block will get executed when user clicks on "clear" button
        elif 'clear' in request.POST:
            clear_alarm(request)

            blocks = {'message': 'clear'}
            return store_time(request, blocks)

        else:
            stop_alarm(request)

            blocks = {'message': 'Stop'}
            return store_time(request, blocks)

    else:
        return render(request, 'test.html', blocks)


def set_alarm(request):
    alarm_data = request.POST.get('alarm_data')

    Timer.objects.update_or_create(id=1, defaults={'timer': alarm_data}, )

    timer_data = Timer.objects.get(id=1)

    return timer_data.timer;


def clear_alarm(request):
    # Clear record
    Timer.objects.all().delete()


def stop_alarm(request):
    logging.warning("stop_alarm")
    
    device.turn_off()
    # led.off()
    
    pygame.mixer.music.stop()

def call_scheduler(request, timer_data):
    scheduler = BackgroundScheduler(timezone='Asia/Kolkata')

    scheduler.add_job(test, next_run_time=timer_data, args=[request])
    scheduler.start()


def store_time(request, blocks):
    return render(request, 'test.html', blocks)


def test(request):
    logging.warning("KALI O KALI")

    device.turn_on()
    
    # led.on()
    
    pygame.mixer.music.load(get_random_songs())
    pygame.mixer.music.play()
    
def get_random_songs():
    
    for path, dirs, files in os.walk(songs_path):
        for f in files:
            songs_collection.append (f)
            
    random_selected_songs = random.choice (songs_collection)
    
    return songs_path + random_selected_songs
