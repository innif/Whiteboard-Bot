from . import motorshield
import time

def run_bot():
    while True:
        for i in range(-100, 100, 1):
            motorshield.set_motor(0, i/100)
            motorshield.set_motor(1, 1-(i/100))
            time.sleep(0.01)

        motorshield.set_motor(0, 0)
        motorshield.set_motor(1, 0)
        time.sleep(2)