# scraper functions that get stats for specific plants
from bs4 import BeautifulSoup
import requests
url = https://garden.org/plants
# use this as baseline

def getStats(string):
    # put the string in the search plants field
    # run
    # look under table that has 'search results' and click first option

    # parse table to find the following stats:
    # - Life cycle 
    # - Sun requirement 
    # - Water preferences

    # return a list called plantStat with the parameters [lifeCycle, sunReqs, waterPreference]

def getAction([lifeCycle, sunReqs, waterPreference]):
    # based on these parameters, make a daily cycle for how the following hardware must work
    # mister
    # night shade
    # LED simulations
    # Humidity intake + thresholds / limits
    # how long can lid be taken off
    # 
    return null;
