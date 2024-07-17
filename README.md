# A Real Fall Damage Simulator!

# Inspiration:
This was just a project I decided to do for fun off a random thought gaming on a saturday night. Have you every played a game so difficult you wondered if physical pain would be better? Chained Together, is the game that inspired this project and is compatible for but reasonable adjuments could easily bemade as this is just a Proof of Concept and fun invention and my no means a fully formed product. Anyways There are some physical requirements but the code for this is very simple. 1 program runs on the clinet (my laptop) which will track the current height of my character in the game by uusinng OCR to read the height displayed on the screen, this script will also send an http request message to my server at the /electrocute route... Now the Server is the fun part! The server is just a Raspberry Pi running on python flask that will accept an http request and preforn the neccasary movments of a servo to turn an ems device on that tazes the user. I was unfimilar with electrical engeneering and didnt want to learn it in a week(personal deadline) so I chose a crude physical interface instead of a relay or alternative to control current. This makes the device relively safe if testied and used with concern for the users wellbeing.

## What?

This is just some code that can help you get tazed everytime you fall in chained together. Yup thats its. You need physical stuff too of course.

# Material
- Raspberry Pi 5
- 9g MS18 180* Servo
- 3 M-F Jumper Cable
- Computer with "Chained Together" Installed and ready to play!

# Setup
- If your intrested in recreating this device PLEASE use caution and follow my youtube video : Comming soon
- - Too setup this project please make a venv ONLY ON THE CLIENT PLAYING THE GAME, if you create a venv on the rasPI everything will stop working keep this in mind
- Once the venv is created download the dependancies from the requirements.txt file
- 

# Usage:
- Before you begin learn how to use an EMS device and strap in!
- First make sure "Chained Together" is open (also go above height 0 if you dont want to get tazed immidiently)
- SSH into the raspberry pi and run "python real_electrocution_server.py" to make the electrocutiono server start listening to requests
- Run "python fall_tracker.py"
- Play chained together and do you absolute best knowing falling means not only mental torture but physical torture to!!!!
- 
## Notes
- I used an EMS device, please use caution as these can be dangerous for people with heart conditions. This was for fun, please do not blame me for any harm caused by recreating this. I only post on github for the sovereign sake of Open-Source knowlegde.
- I sm not finished using the device yet, althought development is mostly finished, all other code files will be uploaded soon. Thanks for reading and i hope you enjoyed!
