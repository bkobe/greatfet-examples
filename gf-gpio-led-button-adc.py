#!/usr/bin/python3

import time
from greatfet import GreatFET

# Function to take adc sample to turn on/off LEDs
# A bit simple, and not optimized, but it works
# --Future work, optimize by building a pin array list?
def LightDisplay(adc_sample):
	if adc_sample > 100:
		led1.write(True)
	else:
		led1.write(False)

	if adc_sample > 200:
		led2.write(True)
	else:
		led2.write(False)

	if adc_sample > 300:
		led3.write(True)
	else:
		led3.write(False)

	if adc_sample > 400:
		led4.write(True)
	else:
		led4.write(False)

	if adc_sample > 500:
		led5.write(True)
	else:
		led5.write(False)

	if adc_sample > 600:
		led6.write(True)
	else:
		led6.write(False)

	if adc_sample > 700:
		led7.write(True)
	else:
		led7.write(False)

	if adc_sample > 800:
		led8.write(True)
	else:
		led8.write(False)

	if adc_sample > 900:
		led9.write(True)
	else:
		led9.write(False)


## Start of MAIN CODE ##
gf = GreatFET()

# Setup the LEDs to output a bargraph-type output
led1 = gf.gpio.get_pin('J1_P3')
led1.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

led2 = gf.gpio.get_pin('J1_P4')
led2.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

led3 = gf.gpio.get_pin('J1_P5')
led3.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

led4 = gf.gpio.get_pin('J1_P6')
led4.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

led5 = gf.gpio.get_pin('J1_P7')
led5.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

led6 = gf.gpio.get_pin('J1_P8')
led6.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

led7 = gf.gpio.get_pin('J1_P9')
led7.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

# There is no P11 for GPIO, 10 and 12 are skipped to avoid
# contention with bootloader modes (inputs)

led8 = gf.gpio.get_pin('J1_P13')
led8.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

led9 = gf.gpio.get_pin('J1_P14')
led9.set_direction(gf.gpio.DIRECTION_OUT)
led1.write(False)

# Setup the push button input to read voltage state
button = gf.gpio.get_pin('J1_P15')
button.set_direction(gf.gpio.DIRECTION_IN)
buttonstate = button.read()

# Main Loop for code to cycle through
while(True):
	#If the display LEDs are off (zero ADC input), button lights
	# first LED for 1 second
	buttonstate = button.read()
	if buttonstate == True:
		led1.write(True)
		time.sleep(1.0)
		led1.write(False)

	# Get one sample from the ADC, and convert the first number
	# returned in the tuple to an integer for comparison
	adc_sample = int(gf.adc.read_samples(1)[0])
	LightDisplay(adc_sample)

	# Toggle the on-board LED as a heartbeat that it's running
	# in the while loop
	gf.leds[4].toggle()
	time.sleep(0.1)
