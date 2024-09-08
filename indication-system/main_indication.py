#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

led_trigger_path = '/sys/class/leds/PWR/trigger'
button_pin = 17

def set_led_trigger(trigger):
    try:
        with open(led_trigger_path, 'w') as f:
            f.write(trigger)
    except Exception as e:
        print(f"Error: {e}")

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up 

try:
    prev_state = None
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            state = 'default-on'
        else:
            state = 'none'

        if prev_state != state:
            set_led_trigger(state)
            prev_state = state

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()