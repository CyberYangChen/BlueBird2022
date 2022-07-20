# -*- coding: UTF-8 -*-

#CyberYang
#https://github.com/timofurrer/w1thermsensor

from w1thermsensor import W1ThermSensor, Sensor

def GetTemp():
    sensor_outside = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-031913c6c1aa")
    temperature_in_celsius = sensor_outside.get_temperature()
    result = temperature_in_celsius
    return result