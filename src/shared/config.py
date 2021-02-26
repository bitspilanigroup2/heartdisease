import configparser
import os
from src.shared.constants import CONFIG_PATH

def loadConfig():
    config = configparser.ConfigParser()
    config.read(os.getcwd() + CONFIG_PATH)
    return config