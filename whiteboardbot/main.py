from . import motorshield
import time
from flask import Flask

def run_bot():
    app=Flask(__name__)

    @app.route('/')
    def index():
        return "Hey!"   
        
    @app.route('/motor/<id>/<power>') 
    def handle_request(id: str, power: str):
        id = int(id)
        power = int(power)/100
        print(f"Motor {id} Power {power}")
        motorshield.set_motor(id, power)
        return "OK 200"   
                                
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)