import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/components/config.ini')


def get_properties(sectionName):
    return config[sectionName]
