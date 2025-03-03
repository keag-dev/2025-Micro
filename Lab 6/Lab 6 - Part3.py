import utime
import machine
import urandom

led = machine.Pin(15, machine.Pin.OUT)
red_button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
yellow_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

fastest_button = None

def button_handler(pin):
    red_button.irq(handler=None)
    yellow_button.irq(handler=None)
    global fastest_button
    fastest_button = pin

led.on()
utime.sleep(urandom.uniform(3, 8))
led.off()
red_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
yellow_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while not fastest_button:
    utime.sleep(0.1)
if fastest_button == red_button:
    print("Red Wins!")
else:
    print("Yellow Wins!")



