import pyttsx3
engine = pyttsx3.init()

## Rate ##
rate = engine.getProperty("rate")
print(rate)
engine.setProperty("rate", 150)
engine.say("Hello I am uttam pun developer. I am learning python")
engine.runAndWait()