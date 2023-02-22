import math
import datetime
def get_time_from_creating(date):
    current_date = datetime.datetime.now()
    if date.tzinfo is not None:
        date = date.replace(tzinfo=None)
    difference = current_date - date
    difference = difference.total_seconds()
    difference-=7200
    unit = 'seconds'
    if difference>60:
        difference/=60
        unit = 'minutes'
    if difference>60 and unit=='minutes':
        difference/=60
        unit = 'hours'
    if difference>24 and unit=='hours':
        difference/=24
        unit = 'days'
    if difference>7 and unit=='days':
        difference/=7
        unit = 'weeks'
    if math.floor(difference)==1:
        unit = unit[:-1]
    if unit=='seconds':
        unit = 'секунди'
    elif unit=='minutes':
        unit = 'минути'
    elif unit=='hours':
        unit = 'часа'
    elif unit=='days':
        unit = 'дни'
    elif unit=='weeks':
        unit = 'седмици'
    elif unit=='second':
       unit = 'секундa' 
    elif unit == 'minute':
        unit='минута'
    elif unit=='hour':
        unit = 'час'
    elif unit == 'day':
        unit = 'ден'
    elif unit == 'week':
        unit = 'седмица'
    return str(math.floor(difference)), unit