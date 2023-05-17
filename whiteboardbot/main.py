from . import motorshield
import time

def run_bot():
    for i in range(100):
        motorshield.set_motor(0, i/100)
        motorshield.set_motor(1, 1-(i/100))
        time.sleep(0.01)

    
    motorshield.set_motor(0, 0)
    motorshield.set_motor(1, 0)