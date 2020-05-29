#!/usr/bin/python3

# Simple GreatFET One example using I2C functions and ThingM BlinkM
# B. Kobe - March, 2020

# Imports for python
import time
from greatfet import GreatFET

# "Constants" to define some standard things
BLINKM_ADDRESS = 0x09
BLINKM_CMD_SETCOLOR = 0x6e
BLINKM_CMD_GETCOLOR = 0x67
BLINKM_CMD_FADECOLOR = 0x63
BLINKM_CMD_STOPSCRIPT = 0x6f

# Create instance of the GreatFET object
gf = GreatFET()

# Stop the BlinkM script (color fading on startup)
# -- need to figure out I2C clock. Previous code of GF used three speeds.
# -- IT works for now, so it must be slow enough for the BlinkM.
gf.i2c.write(BLINKM_ADDRESS,[BLINKM_CMD_STOPSCRIPT])

# Set the BlinkM to a set color and write to board
BlinkM_Red = 0x10
BlinkM_Green = 0x10
BlinkM_Blue = 0x10
gf.i2c.write(BLINKM_ADDRESS,[BLINKM_CMD_SETCOLOR,BlinkM_Red,BlinkM_Green,BlinkM_Blue])

# Now read the color back from the board
gf.i2c.write(BLINKM_ADDRESS,[BLINKM_CMD_GETCOLOR])		# Write one byte of the command we want
print('Set color to: ' + str(gf.i2c.read(BLINKM_ADDRESS,3)))	# Read back the next three bytes

time.sleep(5.0)

while(True):
	BlinkM_Red = 0xFF
	BlinkM_Green = 0x00
	BlinkM_Blue = 0x00
	gf.i2c.write(BLINKM_ADDRESS,[BLINKM_CMD_SETCOLOR,BlinkM_Red,BlinkM_Green,BlinkM_Blue])
	time.sleep(1.0)

	BlinkM_Red = 0x00
	BlinkM_Green = 0xFF
	BlinkM_Blue = 0x00
	gf.i2c.write(BLINKM_ADDRESS,[BLINKM_CMD_SETCOLOR,BlinkM_Red,BlinkM_Green,BlinkM_Blue])
	time.sleep(1.0)

	BlinkM_Red = 0x00
	BlinkM_Green = 0x00
	BlinkM_Blue = 0xFF
	gf.i2c.write(BLINKM_ADDRESS,[BLINKM_CMD_SETCOLOR,BlinkM_Red,BlinkM_Green,BlinkM_Blue])
	time.sleep(1.0)

