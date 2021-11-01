import pyttsx3
friend = pyttsx3.init()
friend.say("Hey, welcome!")
friend.runAndWait()

speech = input("Say something ")
friend.say(speech)
friend.runAndWait()