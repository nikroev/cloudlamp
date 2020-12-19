from datetime import *
from suntime import Sun
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

PLACE = "speyer"

def set_time_zone(place):
    location = geolocator.geocode(place)

    latitude = location.latitude
    longitude = location.longitude
    sun = Sun(latitude, longitude)

    time_zone = datetime.now().date()

    return time_zone, sun

def get_sunrise(time_zone, sun):
    sun_rise = sun.get_local_sunrise_time(time_zone)
    return sun_rise

def get_sunset(time_zone, sun):
    sun_set = sun.get_local_sunset_time(time_zone)
    return sun_set

def get_sunup(sunrise, sunset):
    sunup = sunset - sunrise - timedelta(hours = 2)
    return sunup

def get_period(sunup):
    period_in_sec = sunup.total_seconds() / 3
    period_in_min = period_in_sec / 60
    period_min = period_in_min % 60
    period = timedelta(minutes = period_in_min)
    return period

def get_startSunrise(sunrise):
    startSunrise = sunrise - timedelta(minutes=30)
    return startSunrise

def get_startMorning(sunrise):
    startMorning = sunrise + timedelta(minutes = 30)
    return startMorning

def get_startMidday(startMorning, period):
    startMidday = startMorning + period
    return startMidday

def get_startEvening(startMidday, period):
    startEvening = startMidday + period
    return startEvening

def get_startSunset(sunset):
    startSunset = sunset - timedelta(minutes = 30)
    return startSunset

def get_startNight(sunset):
    startNight = sunset + timedelta(minutes = 30)
    return startNight

def get_setting(startSunrise, startMorning, startMidday, startEvening, startSunset, startNight):

    startSunrise = startSunrise.strftime('%Y-%m-%d %H:%M')
    startSunrise = str(startSunrise)

    startMorning = startMorning.strftime('%Y-%m-%d %H:%M')
    startMorning = str(startMorning)

    startMidday = startMidday.strftime('%Y-%m-%d %H:%M')
    startMidday = str(startMidday)

    startEvening = startEvening.strftime('%Y-%m-%d %H:%M')
    startEvening = str(startEvening)

    startSunset = startSunset.strftime('%Y-%m-%d %H:%M')
    startSunset = str(startSunset)

    startNight = startNight.strftime('%Y-%m-%d %H:%M')
    startNight = str(startNight)

    time = datetime.now()
    time = time.strftime('%Y-%m-%d %H:%M')

    if startSunrise < time < startMorning:
        showSunrise()
    elif startMorning < time < startMidday:
        showMorning()
    elif startMidday < time < startEvening:
        showMorning()
    elif startEvening < time < startSunset:
        showEvening()
    elif startSunset < time < startNight:
        showSunset()
    elif startNight < time < startSunrise:
        showNight()


def showSunrise():
    print("Sunrise")

def showMorning():
    print("morning")

def showMidday():
    print("morning")

def showEvening():
    print("evening")

def showSunset():
    print("sunset")
def showNight():
    print("its night mfs")

TIME_ZONE, SUN = set_time_zone(PLACE)
print("test", TIME_ZONE, SUN)

SUNRISE = get_sunrise(TIME_ZONE, SUN)
SUNSET = get_sunset(TIME_ZONE, SUN)
PERIOD = get_period(get_sunup(SUNRISE, SUNSET))

print("sunrise: ", SUNRISE)
print("sunset: ", SUNSET)

startSunrise = get_startSunrise(SUNRISE)
startMorning = get_startMorning(SUNRISE)
startMidday = get_startMidday(startMorning, PERIOD)
startEvening = get_startEvening(startMidday, PERIOD)
startSunset = get_startSunset(SUNSET)
startNight = get_startNight(SUNSET)

get_setting(startSunrise, startMorning, startMidday, startEvening, startSunset, startNight)

input = input("")
