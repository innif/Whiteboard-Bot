from . import motorshield
import time
from flask import Flask

def run_bot():
    app=Flask(__name__)

    @app.route('/')
    def index():
        return "Hey!"   
        
    @app.route('/motor/<id>/<power>') 
    def handle_request(motor_id: str, power: str):
        motor_id = int(motor_id)
        power = int(power)/100
        print(f"Motor {motor_id} Power {power}")
        motorshield.set_motor(motor_id, power)
        return "OK 200"   

    
    motorshield.set_motor(1, 1)
    time.sleep(2)
    motorshield.set_motor(1, 0)                      
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)