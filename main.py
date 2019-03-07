import sys
import time
import datetime
import telepot


# Connecting config
Config = configparser.ConfigParser()
Config.read('config.ini')
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1
global TGtoken
global TStoken
TGtoken = ConfigSectionMap("Tokens")['telegram']
TStoken = ConfigSectionMap("Tokens")['thingspeak']