from . import motorshield
import time
from flask import Flask

def run_bot():
    app=Flask(__name__)

    @app.route('/')
    def index():
        return "Hey!"   
        
    @app.route('/<actionid>') 
    def handleRequest(actionid):
        print("actionid : {}".format(actionid))
        return "OK 200"   
                                
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)