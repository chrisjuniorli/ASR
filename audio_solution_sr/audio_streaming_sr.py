import argparse
#from distutils.util import strtobool
#import json
#import requests
import os
import speech_recognition as sr
import sys
import pdb

class AudioStreamingSR:

    def __init__(self):
        """
        Initialization
        """
        self.r = None 
        self.mic = None
        self.mic_timeout = 30
        self.phrase_time_limit = 30
        self.RED = '\u001b[31m'
        self.GREEN = '\u001b[32m'
        self.YELLOW = '\u001b[33m'
        self.PURPLE = '\u001b[35m'
        self.CYAN = '\u001b[36m'
        self.RESET = '\u001b[0m' 
    
    def parse_args(self):
        parser = argparse.ArgumentParser(description='Parse Zoom CC options')
        args, unknown = parser.parse_known_args()

    def create_recognizer(self):
        """
        Create recognizer objects
        """
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def main(self):
        """
        Run speech recognition / POST loop
        """
        self.create_recognizer()
        while True:
            try:
                with self.mic as source:
                    #self.r.adjust_for_ambient_noise(source)
                    self.r.energy_threshold = 30
                    print('Energy threshold={}'.format(self.r.energy_threshold))
                    print('{}Say something (or press ctrl+C to exit) {}'.format(self.PURPLE,self.RESET))
                    try:
                        audio = self.r.listen(source,
                            timeout=self.mic_timeout, phrase_time_limit=self.phrase_time_limit)
                        print('Transcribing...')
                        self.payload = self.r.recognize_google(audio, language='en-US')
                        #self.payload = r.recognize_sphinx(audio)
                    except KeyboardInterrupt:
                        break
                    except sr.WaitTimeoutError:
                        print("Timeout error, continuing...")
                        continue
                    except sr.UnknownValueError:
                        print("Nothing said, continuing...")
                        continue
                    except:
                        print('{}Unexpected error: {}{}'.format(self.RED, sys.exc_info()[0], self.RESET))
                        raise
                print("{}: {} {}".format(self.GREEN, self.payload, self.RESET))
                #self.post_transcript(self.payload)
            except KeyboardInterrupt:
                break

if __name__ == '__main__':
    ASR = AudioStreamingSR()
    ASR.main()