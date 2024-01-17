import random
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class foodgen:
    #Morning tiffin
    def morning(c):
        speak("Making uupppma is not advicable by the creator of th app , Therefore it is not included in the list of items")

        y=["idili","dosa","POORI","pongal","idiyappam","chappati","kuzhi panniyaram"]
        z=len(y)
        x=random.randrange(0,z)
        return y[x]
    def sambar(b):
        y=["parupu sambar","arachi kodina sambar","venthiyam sambar","vaatha kozhambu","kara kozhambu","chappati","puli kozhambu"]
        z=len(y)
        x=random.randrange(0,z)
        return y[x]
    def curry(b):
        y=["potato fry ","ladies finger","brinjal","sweet potato","kara kozhambu","chappati","puli kozhambu"]
        z=len(y)
        x=random.randrange(0,z)
        return y[x]
    def rasam(b):
        y=["parupu sambar","arachi kodina sambar","venthiyam sambar","vaatha kozhambu","kara kozhambu","chappati","puli kozhambu"]
        z=len(y)
        x=random.randrange(0,z)
        return y[x]
    def snacks(b):
        y=["parupu sambar","arachi kodina sambar","venthiyam sambar","vaatha kozhambu","kara kozhambu","chappati","puli kozhambu"]
        z=len(y)
        x=random.randrange(0,z)
        return y[x]
    def dinnner(b):
        y=["parupu sambar","arachi kodina sambar","venthiyam sambar","vaatha kozhambu","kara kozhambu","chappati","puli kozhambu"]
        z=len(y)
        x=random.randrange(0,z)
        return y[x]
    





    
        
    

    

















