# Simple demo of reading and writing the time for the PCF8523 real-time clock.
# Change the if False to if True below to set the time, otherwise it will just
# print the current date and time every second.  Notice also comments to adjust
# for working with hardware vs. software I2C.

import time
import board
# For hardware I2C (M0 boards) use this line:
import busio as io
# Or for software I2C (ESP8266) use this line instead:
#import bitbangio as io

import adafruit_pcf8523

# Change to the appropriate I2C clock & data pins here!
i2c_bus = io.I2C(board.SCL, board.SDA)

# Create the RTC instance:
rtc = adafruit_pcf8523.PCF8523(i2c_bus)

# Lookup table for names of days (nicer printing).
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


#pylint: disable-msg=bad-whitespace
#pylint: disable-msg=using-constant-test
if False:   # change to True if you want to set the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2019,  8,   11,   23,  33,  5,    0,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    print("Setting time to:", t)     # uncomment for debugging
    rtc.datetime = t
    print()
#pylint: enable-msg=using-constant-test
#pylint: enable-msg=bad-whitespace

# Main loop:
while True:
    t = rtc.datetime
    #print(t)     # uncomment for debugging
    print("The date is {} {}/{}/{}".format(days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year))
    print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(1) # wait a second
