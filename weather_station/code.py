import time
import board
import busio

#import gc

# Water temperature
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20 # water temperature sensor
ow_bus = OneWireBus (board.D5)
ds18 = DS18X20 (ow_bus, ow_bus.scan()[0])

# I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Clock
#import adafruit_pcf8523 #clock
#clock  = adafruit_pcf8523.PCF8523(i2c)

# Light sensor
#import adafruit_tsl2591 # light sensor
#light_sensor = adafruit_tsl2591.TSL2591(i2c)
#light_sensor.gain = adafruit_tsl2591.GAIN_LOW

# Multi sensor
#import adafruit_bme680
#multi = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug = False)

# UV sensor
#import adafruit_veml6075
#uv_sensor = adafruit_veml6075.VEML6075(i2c)

#uv_index_max = 0
#lux_max = 0
#lux_min = light_sensor.lux
water_temp_max = ds18.temperature
water_temp_min = water_temp_max
while True:
    #print(gc.mem_free())
    #t = clock.datetime
    #print('Tue {}.{}.{} {}:{}:{:02}'.format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec))
    #print('Tue {}.{}.{} {}:{}:{:02} T = {} C \tLight = {} lux'.format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec))
    #print('T_water = {} C \tLight = {} lux\tT_air = {}'.format(ds18.temperature, light_sensor.lux, multi.temperature))
    water_temp = ds18.temperature
    if water_temp > water_temp_max:
        water_temp_max = water_temp
    if water_temp < water_temp_min:
        water_temp_min = water_temp
    print("Temperature:{} C (max.: {}, min.: {})".format(water_temp, water_temp_max, water_temp_min))
    #print('T_air = {:.1f} C \tp = {} hPa \th = {:.2f} m \tR = {} Ohm'.format(multi.temperature, multi.pressure, multi.altitude, multi.gas))
    """uv_index = uv_sensor.uv_index
    if uv_index > uv_index_max:
        uv_index_max = uv_index
    lux = light_sensor.lux
    if lux > lux_max:
        lux_max = lux
    if lux < lux_min:
        lux_min = lux"""
    #print('\tUV = {} (max.: {})'.format(uv_index, uv_index_max))
    #print("Light: {} lux\t(max.: {}, min.: {})\tUV = {}\t(max.: {})".format(lux, lux_max, lux_min, uv_index, uv_index_max))
    #print("Light: {} lux\t(max.: {}, min.: {})\tUV = {}\t(max.: {})".format(lux, lux_max, lux_min, uv_index, uv_index_max))
    #print("Light: {} lux\t(max.: {}, min.: {})\tUV = {}\t(max.: {})".format(lux, lux_max, lux_min, uv_index, uv_index_max))
    #print(lux)
    time.sleep(1.0)