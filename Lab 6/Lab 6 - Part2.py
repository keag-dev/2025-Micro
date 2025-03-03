import utime
import machine
import urandom

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    button.irq(handler=None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print("Your reaction time was "+str(timer_reaction)+" milliseconds!")
    
led.on()
utime.sleep(urandom.uniform(3, 8))
led.off()
timer_start = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
    