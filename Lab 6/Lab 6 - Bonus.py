import utime
import machine
import urandom

led = machine.Pin(15, machine.Pin.OUT)
red_button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
yellow_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

fastest_button = None
reaction_time1 = None
reaction_time2 = None

def button_handler1(pin):
    red_button.irq(handler=None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    global fastest_button
    if not fastest_button:
        fastest_button = pin
    global reaction_time1
    if not reaction_time1:
        reaction_time1 = timer_reaction
        print(timer_reaction)
    else:
        global reaction_time2
        reaction_time2 = timer_reaction
        print(timer_reaction)

def button_handler2(pin):
    yellow_button.irq(handler=None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    global fastest_button
    if not fastest_button:
        fastest_button = pin
    global reaction_time1
    if not reaction_time1:
        reaction_time1 = timer_reaction
        print(timer_reaction)
    else:
        global reaction_time2
        reaction_time2 = timer_reaction
        print(timer_reaction)

led.on()
utime.sleep(urandom.uniform(3, 8))
led.off()
timer_start = utime.ticks_ms()
red_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler1)
yellow_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler2)

while not fastest_button:
    utime.sleep(0.1)
while not reaction_time1:
    utime.sleep(0.1)
while not reaction_time2:
    utime.sleep(0.1)
    
if fastest_button == red_button:
    print("Red Wins! Time was: "+str(reaction_time1)+" ms")
    print("Yellow time was: "+str(reaction_time2)+" ms")
else:
    print("Yellow Wins! Time was: "+str(reaction_time1)+" ms")
    print("Red time was: "+str(reaction_time2)+" ms")