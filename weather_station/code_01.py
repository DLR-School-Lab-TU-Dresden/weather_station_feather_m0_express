import time
import board
import busio

#from adafruit_onewire.bus import OneWireBus

# I2C sensors
#from adafruit_ds18x20 import DS18X20 # water temperature sensor
#import adafruit_tsl2591 # light_sensor
#import adafruit_pcf8523 #clock
#import adafruit_bme680
import adafruit_veml6075

i2c = busio.I2C(board.SCL, board.SDA)
#light_sensor = adafruit_tsl2591.TSL2591(i2c)
#clock  = adafruit_pcf8523.PCF8523(i2c)
#multi = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug = False)
uv_sensor= adafruit_veml6075.VEML6075(i2c)

#ow_bus = OneWireBus (board.D5)
#ds18 = DS18X20 (ow_bus, ow_bus.scan()[0])

while True:
    #t = clock.datetime
    #print('Tue {}.{}.{} {}:{}:{:02} T = {} C \tLight = {} lux'.format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec, ds18.temperature, light_sensor.lux))
    #print('Tue {}.{}.{} {}:{}:{:02} T = {} C \tLight = {} lux'.format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec))
    #print('T_water = {} C \tLight = {} lux\tT_air = {}'.format(ds18.temperature, light_sensor.lux, multi.temperature))
    #print('Light = {:.1f} lux\tT_air = {:.1f} C \tp = {} hPa \th = {:.2f} m \tR = {} Ohm \tUV = {}'.format(light_sensor.lux, multi.temperature, multi.pressure, multi.altitude, multi.gas, uv_sensor.uv_index))
    print('UV = {}'.format(uv_sensor.uv_index))
    time.sleep(1.0)
