"""
            Author:  Rowland DePree                             Camera_Detection.py

            This is a program designed to detected whenever your integrated camera goes on. This was designed
            with laptops in mind, but could possibly be used with computers with ONLY ONE CAMERA.  The program
            will check every x amount of time (where x is the user inputted in seconds).  If the camera is detected as
            being on, then a pop-up message will appear and ask for the user to re-enter a second count in case the camera
            was turned on by the user.
"""

import time
import cv2
from easygui import msgbox


def main():
    """
    This is the main method, where the camera state is detected and a possible pop-up message will be sent.
    :return:
    """
    cap = cv2.VideoCapture(0)

    turn_msgbox_on = validate(raw_input('Enter the check frequency for camera detection (Seconds): '))

    while True:
        time.sleep(float(turn_msgbox_on))
        if cap.open(0):
            msgbox('YOUR CAMERA HAS BEEN TURNED ON', 'Camera Detection')
            turn_msgbox_on = validate(raw_input('Re-Enter the check frequency for camera detection (Seconds): '))


def validate(user_input):
    """
    A validation method to make sure the user has inputted a number greater than 0 seconds
    :param user_input:
    :return:
    """
    valid = False
    while not valid:
        if user_input < 0:
            print('INVALID ENTRY!  THE TIME CANNOT BE LESS THAN 0 SECONDS!')
            user_input = raw_input('Re-Enter the check frequency for camera detection (Seconds): ')
        else:
            valid = True
    return user_input


'''
    Starts the main program
'''
if __name__ == '__main__':
    main()
