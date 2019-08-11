# Simple GPS datareading demonstration.
# This actually doesn't even use the GPS library and instead just reads raw
# NMEA sentences from the GPS unit and prints them.
import board
import busio

# Define RX and TX pins for the board's serial port connected to the GPS.
# These are the defaults you should use for the GPS FeatherWing.
# For other boards set RX = GPS module TX, and TX = GPS module RX pins.
RX = board.RX
TX = board.TX

# Create a serial connection for the GPS connection using default speed and
# a slightly higher timeout (GPS modules typically update once a second).
uart = busio.UART(TX, RX, baudrate=9600, timeout=30)

# Main loop just reads data from the GPS module and prints to serial output.
while True:
    sentence = uart.readline()
    print(str(sentence, 'ascii').strip())
