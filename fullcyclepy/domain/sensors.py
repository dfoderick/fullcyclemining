'''Sensor entities'''
import datetime

class Sensor(object):
    """A Sesnor"""
    def __init__(self, sensorid='', sensortype='', location=''):
        self.sensortype = sensortype
        #it is expected that from sensorid could be found location, type and other details
        self.sensorid = sensorid
        self.location = location


class SensorValue(object):
    """A Sesnor Reading"""

    def __init__(self, sensorid='', value='', valuetype='', sensor=None, sensortime=datetime.datetime.utcnow()):
        self.sensorid = sensorid
        self.valuetype = valuetype
        self.value = value
        self.sensor = sensor
        self.sensortime = sensortime
