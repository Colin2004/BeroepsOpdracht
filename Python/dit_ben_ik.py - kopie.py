#Dit is de tweede versie van ditbenik.py
#In deze versie verander ik het verhaal van linear naar veelzijdig.
#Dit houd in dat er meerende uitkomsten zijn.

print("Hello You!, ik ben Colin")
print("Wie ben jij?")
name = input("Type je naam hier: ")
print("Hello " + name)
print("")
print("Ik ben een nieuwkomer op het Mediacollege.")
print("Om mij beter te kennen ga ik wat vragen stellen.")

print("")
print("Oke de eerste vraag.")
print("In welke stad woon ik?")
print("A: Purmerend")
print("B: Heerhugowaard")
print("C: Zaandam")
Antwoord_1 = input("Type hier je antwoord: ")

if Antwoord_1 == "A" :
	print("Klopt ik woon in purmerend.")
elif Antwoord_1 == "B" :
	print("Helaas! Ik ben wel in Heerhugowaard geboren.")
elif Antwoord_1 == "C" :
	print("Helaas! Ik heb wel in Zaandam gewoond.")

print("")


print("volgende vraag:")
print("Welke game speel ik het liefst?")
print("A: Minecraft")
print("B: Rainbow six siege")
print("C: Forza Horizon 4")
Antwoord_2 = input("Type hier je antwoord: ")

if Antwoord_2 == "A" :
	print("Nee! maar ik vind het wel een leuk spel vooral vroeger.")
elif Antwoord_2 == "B" :
	print("Klopt! Ik speel dit spel het lieftst met vrienden in mijn vrije tijd.")
elif Antwoord_2 == "C" :
	print("Nee! maar ik speel het wel graag op de laptop.")

print("")


print("Nu wordt het leuk.")
print("Als je deze vraag goed hebt krijg je er nog 1 extra, anders heb je pech!")
print("Op welke sport zit ik?")
print("A: Judo")
print("B: Voetbal")
print("C: Waterpolo")
route_1 = False
Antwoord_3 = input("Type hier je antwoord: ")
if Antwoord_3 == "A" :
	print("Helaas! Ik heb er wel op gezeten")
	
elif Antwoord_3 == "B" :
	print("Helaas! Ik heb er wel op gezeten")
	
elif Antwoord_3 == "C" :
	print("Dat klopt!")
	route_1 = True
print("")

if route_1 == True:
        print("Gefeliciteerd je hebt de vorige vraag goed!")
        print("Dan komt nu de extra vraag.")
        print("Welke afkomst heb ik?")
        print("A: Nederlands/Engels")
        print("B: Nederlands/Duits")
        print("C: Alleen Nederlands")
        antwoord_route_1 = input("Type hier je antwoord: ")
        if antwoord_route_1 == "A":
                print("Dat klopt! Ik heb namelijk een Engelse moeder!")
        elif antwoord_route_1 == "B":
                print("Helaas! Ik heb geen duitse afkomst.")
        elif antwoord_route_1 == "C":
                print("Helaas! Ik heb een ouder van een andere afkomst.")
else:
        print("Jammer! Je hebt niet alle vragen goed beantwoord")
        print("Volgende keer beter!")
print("")
print("Dit is het einde van de quiz")
print("Ik hoop dat je hem leuk vond")




