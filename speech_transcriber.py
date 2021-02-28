#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:55:22 2021

@author: anirvan
"""

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()
# recognize speech using Wit.ai
WIT_AI_KEY = "UOKTFJELS6XDGHJ2UWWFBFJ53D3JNVFG"  # Wit.ai keys are 32-character uppercase alphanumeric strings

try:
    print("Adjusting to background noise...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Setting minimum energy threshold to {}".format(r.energy_threshold))
    print("Start talking now>>")
    consult = ""
    # Add logic here to start consultation when hotword/intent is spoken
    # Intent can be something like: "start session"
    while True:
        print(">>")
        value = ""
        with m as source: audio = r.listen(source)
        try:
            # recognize speech using Wit.ai Speech Recognition
            value = r.recognize_wit(audio, key=WIT_AI_KEY)
            if value is not None: # when some text transcription was received.
                print(">> {}".format(value))
        except sr.UnknownValueError:
            value = "???"
            print("Didn't understand that last part")
        except sr.RequestError as e:
            value = "!!!"
            print("Couldn't request results from Wit.ai Speech Recognition service; {0}".format(e))
            
        # Add logic here to stop consultation when hotword/intent is spoken
        # Intent can be something like: "stop session"
        # On that condition, print out session transcript
        if 'stop session' in value:
            print(">> {}".format(consult))
        else :
            consult = consult + '\n' + value
except KeyboardInterrupt:
    pass