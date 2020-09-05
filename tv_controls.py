import RPi.GPIO as GPIO
import time
from constants import *

GPIO.setmode(GPIO.BCM)

for i in range(len(outputs)):
	GPIO.setup(outputs[i], GPIO.OUT)

def toggle_power():
	GPIO.output(POWER_OUT, GPIO.LOW)
	time.sleep(POWER_TOGGLE_INIT_SLEEP)
	GPIO.output(POWER_OUT, GPIO.HIGH)
	time.sleep(POWER_TOGGLE_INIT_SLEEP)
	GPIO.output(POWER_OUT, GPIO.LOW)
	time.sleep(POWER_TOGGLE_SLEEP)
	GPIO.output(POWER_OUT, GPIO.HIGH)

def adjust_volume(volume_steps):
	pin = VOLUME_UP_OUT

	if volume_steps < 0:
		pin = VOLUME_DOWN_OUT
		volume_steps = abs(volume_steps)

	GPIO.output(pin, GPIO.LOW)
	time.sleep(INIT_SLEEP)
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(INIT_SLEEP)

	for i in range(volume_steps):
		GPIO.output(pin, GPIO.LOW)
		time.sleep(AFTER_SLEEP)
		GPIO.output(pin, GPIO.HIGH)

		if i % 5 == 0:
			time.sleep(AFTER_SLEEP*3)
		else:
			time.sleep(AFTER_SLEEP)