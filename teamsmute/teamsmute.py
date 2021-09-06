from os import environ
from pynput.keyboard import Key, Controller
from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv
import os

class Teams(Resource):
    def post(self):
        sendMuteKeys()
    

def sendMuteKeys():
    print("Mute/Unmute teams.")
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press("m")
    keyboard.release("m")
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

app = Flask(__name__)
app.debug = False
api = Api(app)
api.add_resource(Teams, "/teamsmute")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)

