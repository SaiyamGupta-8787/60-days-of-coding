'''
3. Install an external module and use it to perform an operation of your interest.
'''
import pyttsx3 #* for voice
engine = pyttsx3.init()
engine.say("Hey i am good")
engine.runAndWait()