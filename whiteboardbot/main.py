from . import motorshield
import time

def run_bot():
    for i in range(100):
        motorshield.set_motor(i/100, 0)
        motorshield.set_motor(1-(i/100), 1)
        time.sleep(0.01)