import utime
import machine
import urandom

led = machine.Pin(15, machine.Pin.OUT)
red_button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
yellow_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

fastest_button = None
reaction_time = None

def button_handler(pin):
    red_button.irq(handler=None)
    yellow_button.irq(handler=None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    global fastest_button
    fastest_button = pin
    global reaction_time
    reaction_time = str(timer_reaction)

led.on()
utime.sleep(urandom.uniform(3, 8))
led.off()
timer_start = utime.ticks_ms()
red_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
yellow_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while not fastest_button:
    utime.sleep(0.1)
if fastest_button == red_button:
    print("Red Wins! Time was: "+reaction_time+" ms")
else:
    print("Yellow Wins! Time was: "+reaction_time+ "ms")




