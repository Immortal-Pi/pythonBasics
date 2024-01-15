import argparse
import sys

import pyttsx3
def texttospeech():
    '''
    pyttsx3 is used for text to speech
    :return:
    '''
    engine=pyttsx3.init()
    parser=argparse.ArgumentParser()
    parser.add_argument("-read",help='what to read',type=str)
    this=parser.parse_args()

    engine.say(this.read)
    engine.runAndWait()

    return