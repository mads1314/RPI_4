import logging
import pygame
from tuya.devices import TuyaSmartSwitch

from sample_alarm_latest.components import smart_bulb, songs, read_properties

tuya_properties = read_properties.get_properties('Tuya')

pygame.mixer.init()

# device = TuyaSmartSwitch(username="er.madhav21@gmail.com", password="Password1314", location="EU", device="014033082cf4323237a7")

device = TuyaSmartSwitch(username=tuya_properties['username'], password=tuya_properties['password'], location=tuya_properties['location'],
                         device=tuya_properties['smart_bulb_id'])


def turn_on_alarm():
    logging.warning("KALI O KALI")

    smart_bulb.turn_on(device)
    songs.play_song(pygame)


def turn_off_alarm():
    logging.warning("KALI O KALI")

    smart_bulb.turn_off(device)
    songs.stop_song(pygame)
