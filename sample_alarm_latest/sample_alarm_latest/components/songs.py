import os
import random

from sample_alarm_latest.components import read_properties

songs_collection = []

default_properties = read_properties.get_properties('Default')


def get_random_songs():
    for path, dirs, files in os.walk(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + default_properties['songs_path']):
        for f in files:
            songs_collection.append(f)

    random_selected_songs = random.choice(songs_collection)

    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + default_properties[
        'songs_path'] + random_selected_songs


def play_song(pygame):
    pygame.mixer.music.load(get_random_songs())
    pygame.mixer.music.play()


def stop_song(pygame):
    pygame.mixer.music.stop()
