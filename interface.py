import RPi.GPIO as GPIO
import time

import sys
sys.path.append('../')

from constants import *

GPIO.setmode(GPIO.BCM)

for i in range(len(inputs)):
	GPIO.setup(inputs[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(outputs[i], GPIO.OUT)

try:
	while True:
		for i in range(len(inputs)):
			GPIO.output(outputs[i], GPIO.input(inputs[i]))

		time.sleep(0.05)
except KeyboardInterrupt:
	print('Keyboard interrupt received')
except Exception as e:
	print(f'Caught unexpected exception: {e}')
finally:
	print('Cleaning up')
	GPIO.cleanup()