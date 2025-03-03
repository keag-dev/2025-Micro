import utime
import machine
import urandom

led = machine.Pin(15, machine.Pin.OUT)
button1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button1_handler(pin):
    button1.irq(handler=None)
    print(pin)
    led.on()
    
def button2_handler(pin):
    button2.irq(handler=None)
    print(pin)
    led.off()

while True:
    button1.irq(trigger=machine.Pin.IRQ_RISING, handler=button1_handler)
    button2.irq(trigger=machine.Pin.IRQ_RISING, handler=button2_handler)
    
    