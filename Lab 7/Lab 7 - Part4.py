import machine
import utime

pir1 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
pir2 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_DOWN)

redLed = machine.Pin(15, machine.Pin.OUT)
grnLed = machine.Pin(14, machine.Pin.OUT)

buzzer = machine.Pin(13, machine.Pin.OUT)

def pir_handler(pin):
    #The handler gets the triggered pin that we can compare
    #against our defined pins above
    if pin == pir1:
        print("Alarm! Motion detected in Zone 1!!")
        for i in range (10):
            redLed.toggle()
            utime.sleep_ms(20)
            for j in range (20):
                buzzer.toggle()
                utime.sleep_ms(2)
    elif pin == pir2:
        print("Alarm! Motion detected in Zone 2!!")
            for i in range (10):
                grnLed.toggle()
                utime.sleep_ms(20)
                for j in range (20):
                    buzzer.toggle()
                    utime.sleep_ms(2)
    else:
        print("This should never happen :)")

pir1.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
pir2.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

grnLed.on()
while True:
    redLed.toggle()
    grnLed.toggle()
    utime.sleep(1)