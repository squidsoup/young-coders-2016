#	Blink.py
#
# Interesting pins:
#
# Pin Numbering on Raspberry PIs is a notorious CF
#
#	1 	3.3v
#
#	34	GND
#	39	GND
#
#	33	GPIO13	wpi-23
#	35	GPIO19	wpi-24
#	36	GPIO16	wpi-27
#	37	GPIO26	wpi-25
#	38	GPIO20	wpi-28
#	40	GPIO21	wpi-29
#	
import wiringpi
from time import sleep

wiringpi.wiringPiSetupPhys()	# choose physical pin numbers

#
#	pins 39 and 40 are the last two pins on the raspberry pi 
#	GPIO connector, pin 39 is a ground, pin 40 is a GPIO
#

wiringpi.pinMode(12, 2)		# make pin 40 an output
wiringpi.pinMode(38, 1)		# make pin 40 an output
wiringpi.pinMode(37, 1)		# make pin 40 an output

while (1):
    for i in range(1023):
        wiringpi.pwmWrite(12, i)	# turn pin 40 on

        sleep(0.001)        


while (1):
            
##            wiringpi.pwmWrite(12, 900)	# turn pin 40 on
##            sleep(1)			# wait a while
            wiringpi.digitalWrite(38, 1)	# turn pin 40 on
            sleep(1)			# wait a while
            wiringpi.digitalWrite(37, 1)	# turn pin 40 on
            sleep(1)			# wait a while	
            wiringpi.pwmWrite(12, 200)	# turn pin 40 off
            sleep(1)			# wait a while
            wiringpi.digitalWrite(38, 0)	# turn pin 40 off
            sleep(1)			# wait a while
            wiringpi.digitalWrite(37, 0)	# turn pin 40 off
            sleep(1)			# wait a while

