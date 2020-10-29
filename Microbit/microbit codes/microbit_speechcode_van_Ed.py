from microbit import *
import speech
import random

# hier worden de woorden gedefineerd
# 3 is de lengte van de arrays "onderwerp", en "rest"
# als je meer woorden wilt gebruiken dan moet je de lengte veranderen
lengteWoordArray = 3

# arrays met woorden
onderwerp = ["she", "Ed", "Rosmerta"]
werkwoord = ["Walks", "learns", "drinks"]
rest = ["hard", "at school", "cofee"]

def sayTheWords1(Word):
    print(Word)
    speech.say(Word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)

def sayTheWords2():
    willekeurigGetal = random.randint(0, lengteWoordArray -1)
    display.show(willekeurigGetal)
    sayTheWords1(onderwerp[willekeurigGetal])
    sayTheWords1(werkwoord[willekeurigGetal])
    sayTheWords1(rest[willekeurigGetal])

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        sayTheWords1("hallo i am happy")
    elif button_b.is_pressed():
        display.show(Image.SAD)
        sayTheWords1("why are you sad")
    elif display.read_light_level() <40:
        sayTheWords2()
    else:
        display.show(Image.SQUARE)
