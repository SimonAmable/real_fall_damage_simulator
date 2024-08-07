import pyautogui
import os
import pytesseract
import easyocr
from PIL import Image
import re
import time
import cv2
import requests
import pygame

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

#set path to tessaract.exe (the OCR library we are using)
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)




def easy_image_to_only_number_helper(image_path):
    easy_result = reader.readtext(image_path)
    easyocr_text = ' '.join([result[1] for result in easy_result])
    digits_only = ''.join(re.findall(r'\d', easyocr_text))
    return digits_only

# - FUNCTIONS UNDER HERE
def get_current_height_from_game_screen():
    """
    This function takes in an image file path and returns the number represented by the image. Also does pre-processing of the image
    """
    im = pyautogui.screenshot('images/test.png', region=(0, 50, 102, 25))

    image_path = 'images/test.png'
    image = cv2.imread(image_path)
    
    image_resized = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('images/image_resized.png', image_resized)

    #Image.open(image_path)
     # Check if the image was loaded properly
    if image_resized is None:
        print(f"Error: Could not load image from {image_path}")
        return
    else:
        print(f"Image loaded successfully from {image_path}")
    # Convert to grayscale
    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('images/grayscale.png', gray)

    # # noise removal
    # no_noise =  cv2.medianBlur(image_resized,5)
    # cv2.imwrite('images/no_noise.png', no_noise)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    cv2.imwrite('images/thresh.png', thresh)
    _, thresh_2 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite('images/thresh_2.png', thresh_2)
    
    canny = cv2.Canny(thresh_2, 100, 200)
    cv2.imwrite('images/canny.png', canny)

    # ATTEMPTING TO USE OCR TO READ THE NUMBER FROM PREPROCCESSED IMAGES
    # string_number = pytesseract.image_to_string(thresh)
    cv2.imwrite('images/thresh.png', thresh)
    number_1 = easy_image_to_only_number_helper(thresh)
    number_2 = easy_image_to_only_number_helper(thresh_2)
    number_3 = easy_image_to_only_number_helper(canny)
    #print(f"EASY OCR Height: {number_1} or {number_2} or {number_3}")
    # print(f"Height: {string_number} TESSERACT")
    # Filter out empty strings and convert the remaining strings to integers
    # use the max number found from multiple images as the best guess
    numbers = [int(num.strip()) for num in [number_1, number_2, number_3] if num.strip()]
    best_guess = 0
    if numbers:
        best_guess = max(numbers)
    else:
        best_guess = 0

    # print(f"Best guess: {best_guess}")
    return best_guess




previous_height =0 #predeclare for the if statment

#MAIN UNDER HERE

#make a directory for files if it doesnt exist, and save the screenshot to the directory
if not os.path.exists('images'):
    os.makedirs('images')

#start a while loop to take screenshots of the game screen every 1 second until the user stops the program with the letter 'q'
while True:
    time.sleep(0.5)
    # TODO: Add your code here to track state in the game ( converting image to number)
    current_height = get_current_height_from_game_screen()
    print(f"Current height: {current_height}")

    # TODO: Add your code here to track falling and play a song
    # this can be simple like tracking 3 consecutive decreases in height we should increast polling time 
    
    # TODO: Add your code here to track landing and send an HTTP request
    if current_height <= 11:
        if previous_height  <= 11:
            print("You Landed")
            print("WATCH OUTTT!!!!!!")
            response = requests.post('http://192.168.2.59:5000/electrocute')
        previous_height = current_height
    else:
        previous_height = current_height
        # response = requests.post('http://192.168.2.59:5000/electrocute')
    






#TODO
# 1. Add a function to track when falling is happening to play song
# 2. Add a function to track when landed to send http request to server, see what over fun stuff we can do on a landing event
# 3. To keep track of state in game we just need to loop screen shoots of our hiht constantly and check for changes in the number as that will clearly represent our hieght at all times

# EXTRA EXAMPLE CODE FROM THE LIBRARIES WE USED------------------------
#pyautogui.pause(2.5) # 2.5 seconds pause with this pyautogui lib instead of time.sleep()
#pyautogui.moveTo(0, 0, duration=3)  # move mouse to 0, 0 over a duration of 3 seconds

# Check the screen size
# screen_size = pyautogui.size()
# print(screen_size)


# im = pyautogui.screenshot('images/test.png',region=(0,50, 62, 25))
# with open('images/test.png', 'wb') as f:
#     im.save(f)