#!/usr/bin/python3

import time
from greatfet import GreatFET

## Start of MAIN CODE ##
gf = GreatFET()

# Main Loop for code to cycle through
while(True):
	# ADC 0 is on pin J2_P5
	# Get one sample from the ADC, and convert the first number
	# returned in the tuple to an integer for comparison
	adc_sample = int(gf.adc.read_samples(1)[0])
	print(adc_sample)

	# Toggle the on-board LED as a heartbeat that it's running
	# in the while loop
	gf.leds[4].toggle()
	time.sleep(0.25)

