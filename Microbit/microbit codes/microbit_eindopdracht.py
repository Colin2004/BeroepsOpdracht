from microbit import *
import random

# zorgt ervoor dat de waarde tussen de max en min zit
def check_bounds(val, min, max):
    if val < min:
        val = min
    if val > max:
        val = max
    return val


dx = 50             # de x en y coordinaten van het bolletje
dy = 50             
score = 0           # score (in dit geval level)
speed_y = 0         # de verticale snelheid waarmee het poppetje omhoog gaat
frame = 0           # frame snelheid

# constants
afstand_tussen_platformen = 3   # de afstand tussen de platformen
score_voor_volgend_level = 8   # aantal punten voor volgend level


achtergrond = Image("03330:00000:00033:00000:33333") # De platformen voor op de achtergrond


levels = [30, 25, 20, 18, 15, 12, 10]
current_level = 0

# door deze loop blijven de levels door gaan
while True:
    
    # Dit zorgt ervoor dat het balletje naar beneden valt
    if speed_y < 5:
        speed_y += 1
    dy += speed_y
        
    # naar rechts
    if button_a.is_pressed():
        dx -= 5
    
    # naar links
    if button_b.is_pressed():
        dx += 5
    
    #Dit zorgt ervoor dat de doodle binnen het scherm opduikt en niet daarbuiten
    dy = check_bounds(dy, 0, 99)
    dx = check_bounds(dx, 0, 99)
    
    
    display.show(achtergrond) #dit laat de platformen zien
    
    #Dit zorgt ervoor dat de microbit
    dx_scaled = int(5*dx/100)
    dy_scaled = int(5*dy/100)
    
    
    frame += 1 #extra frame teller 
    
    # de start
    if frame % levels[current_level] == 0:
        score += 1
        achtergrond = achtergrond.shift_down(1)
        
        # naar het volgende level
        if score % score_voor_volgend_level == 0:
            current_level += 1
            display.scroll("Level " + str(current_level + 1))
            if current_level >= len(levels):
                current_level = len(levels) - 1
        
        # cre
        if score % afstand_tussen_platformen == 0:
            platform_start = random.randint(0,3)
            platform_end = random.randint(platform_start + 1, 4)
            for x in range(platform_start, platform_end):
                background.set_pixel(x, 0, 3)
    
    #Dit zorgt ervoor dar het bolletje springt wanneer het op een platform land
    if achtergrond.get_pixel(dx_scaled, dy_scaled) == 3 and speed_y > 2:
        speed_y = -11
        
    # Het spel word hier afgesloten waarneer iemand het platform mist en de grond raakt
    elif dy_scaled == 4:
        display.show(Image.SAD)
        sleep(500)
        display.scroll("Score: " + str(score))
        break
    
    
    display.set_pixel(dx_scaled, dy_scaled, 9) #het uiterlijk van het bolletje
    
    sleep(20)
    
