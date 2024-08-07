# A Real Fall Damage Simulator for the game Chained Together!
# Video Demonstration:
- Comming soon...

# Inspiration:
Quick warning this is a bit of a dumb fun project I decided to do off a random thought gaming on a saturday night. Have you every played a game so difficult you wondered if physical pain would be better? Chained Together, is the game that inspired this project and is compatible for but reasonable adjuments could easily bemade as this is just a Proof of Concept and fun invention and my no means a fully formed product. Anyways There are some physical requirements but the code for this is very simple. 1 program runs on the clinet (my laptop) which will track the current height of my character in the game by uusinng OCR to read the height displayed on the screen, this script will also send an http request message to my server at the /electrocute route... Now the Server is the fun part! The server is just a Raspberry Pi running on python flask that will accept an http request and preforn the neccasary movments of a servo to turn an ems device on that tazes the user. I was unfimilar with electrical engeneering and didnt want to learn it in a week(personal deadline) so I chose a crude physical interface instead of a relay or alternative to control current. This makes the device relitively safe if tested and used with concern for the users wellbeing. Anyways i hope this inspired you to make something better than this but If you enjoyed my creation make sure to like this repo!

## What?

This is just some code that can help you get tazed everytime you fall in chained together. Yup thats its. You will need some physical stuff too make this work.

- real_electrocution_server.py  # This is a simple http server that will listen to requests on the /electrocute route ready to stike me down with the power of Zeus himself. (rate limited at max 1 request per minute for safety)
- fall_tracker.py # This script will take screen shots of the height in game on your moniter, do some preproccesing on the image, and them use Optical Character Recognition (OCR) to keep track of your players height in the game every second.  When you reach a height below 10 (the starting floor) you if will send a request to the server at the  /electocute route. This client side program may also pay some sounds effects when you start falling for lolz.


# Materials
- Raspberry Pi 5 (or any alternative microcontroller with some wireless communication technology and GPIO pins)
- A single 9g MS18 180* Servo (or any alternative this is just the cheapest servo)
- 3 M-F Jumper Cable
- A Computer with "Chained Together" installed

# Setup
- If your intrested in recreating this device PLEASE use caution with the EMS device as they are note entirely safe
- Too setup this project please make a venv ONLY ON THE CLIENT PLAYING THE GAME, if you create a venv on the rasPI everything will stop working keep this in mind
- Once the venv is created download the dependancies from the requirements.txt file
- 


# Usage:
- Before you begin learn how to use an EMS device along with proper safety usage!
- First recreate my diabolical creation in the material word with whatever materials you have and clone repo to use needed files.
- First make sure "Chained Together" is open (also go above height 0 if you dont want to get tazed immidiently)
- SSH into the raspberry pi and run "python real_electrocution_server.py" to make the electrocutiono server start listening to requests
- Run "python fall_tracker.py"
- Play chained together and do you absolute best knowing falling means not only mental torture but physical torture to!!!!
- 
## Notes
- I used an EMS device, please use caution as these can be dangerous for people with heart conditions. This was for fun, please do not blame me for any harm caused by recreating this. I only post on github for the sovereign sake of Open-Source knowlegde.
- I sm not finished using the device yet, althought development is mostly finished, all other code files will be uploaded soon. Thanks for reading and i hope you enjoyed!
