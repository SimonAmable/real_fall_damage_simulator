#THIS PROGRAM WILL HOST A HTTP SERVER TO CONTROL A SERVO ATTACTED TO AN EMS DEVICE, PRESSING THE BUTTON TWICE, SHOCKING THE USER CONNECTED TO THE EMS DEVICE FOR 2 SECONDS

#Imports for Raspberry Pi 
from gpiozero import AngularServo
# Server Imports
from flask import Flask, request
from flask_limiter import Limiter # type: ignore
from flask_limiter.util import get_remote_address # type: ignore
# General Rmports
import time
# all we need to make is a server that presses the button twice, with a 3 second wait inbetween to shock the person (we can make it shorter too)
# add rate limiting so nobody can get shocked rerpeadetdly
# TEST, TEST, TEST : TEST THE TASER DEVICE meticulously and get a perfect 100% testing, I need absolutely no miss fires before i put this on my friends
# Thats it for the server, optimizer the ocr script on the server (identify why it was stalling and make it faster)

# ----------- Functions to control the device -------------------
#

myGPIO = 18
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection) / 1000
minPW = (0.5 - myCorrection) / 1000

servo = AngularServo(myGPIO, initial_angle=0, min_angle=0,
                     max_angle=180, min_pulse_width=minPW, max_pulse_width=maxPW)


def press_button():
    for angle in range(0, 61, 1):  # make servo rotate from 0 to 90 deg
        servo.angle = angle
        time.sleep(SERVO_DELAY_SEC)
    time.sleep(0.5)
    for angle in range(60, -1, -1):  # make servo rotate from 90 to 0 deg
        servo.angle = angle
        time.sleep(SERVO_DELAY_SEC)
    time.sleep(0.5)

def press_button_twice():
    press_button()
    time.sleep(2)
    press_button()

#------------------------------------------------------------------




# Making a server to respond to a request with 1 electrocution

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["1 per 5 minutes"])
@app.route('/')
def home():
    return "Hello, this is your Raspberry Pi Simon! I'm currenty configured as a server to revice request at the /electrocute route which will indeed ELECTROCUTE whoever is connected to this device, be carefull ig..."

@app.route('/electrocute', methods=['POST'])
@limiter.limit("1 per 1 minutes")
def execute():
    # Extract data from the request if needed
    press_button_twice()
    print("WE GOT EM GOOD BOYS")
    return "NIGGA ELECTROCUTED SUCCESSFULLY!", 200

# MAIN CODE UNDER HERE: PLAY THE GAME FIRST, AND THEN RUN THE SERVER!!!!!!!!
if __name__ == '__main__':
    app.run(host='192.168.2.59', port=5000)
