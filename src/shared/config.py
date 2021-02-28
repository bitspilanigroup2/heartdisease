import configparser
import os
from src.shared.constants import CONFIG_PATH

def loadConfig():
    config = configparser.ConfigParser()
    path = os.getcwd() + CONFIG_PATH
    print("printing path " + path)
    config.read(path, encoding="utf-8")
    #config.read(CONFIG_PATH, encoding="utf-8")
    
    return config