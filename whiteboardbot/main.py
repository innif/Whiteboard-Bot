from . import motorshield
import time
from flask import Flask

def run_bot():
    app=Flask(__name__)

    @app.route('/')
    def index():
        return "Hey!"   
        
    @app.route('/motor/<motor_id>/<power>') 
    def handle_request(motor_id: str, power: str):
        motor_id = int(motor_id)
        power = int(power)/100
        print(f"Motor {motor_id} Power {power}")
        motorshield.set_motor(motor_id, power)
        return "OK 200"   
    
    @app.route('/steer/<m1_power>/<m2_power>') 
    def handle_request(m1_power: str, m2_power: str):
        m1_power = int(m1_power)
        m2_power = int(m2_power)
        motorshield.set_motor(0, m1_power)
        motorshield.set_motor(1, m2_power)
        return "OK 200"   
                 
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)