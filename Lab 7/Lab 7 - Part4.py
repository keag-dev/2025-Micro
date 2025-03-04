import machine
import utime

pir1 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
pir2 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_DOWN)

redLed = machine.Pin(15, machine.Pin.OUT)
grnLed = machine.Pin(14, machine.Pin.OUT)

buzzer = machine.Pin(13, machine.Pin.OUT)

alarming = False

def pir_handler(pin):
    #The handler gets the triggered pin that we can compare
    #against our defined pins above
    if pin == pir1:
        print("Alarm! Motion detected in Zone 1!!")
        alarming = True
        for i in range (10):
            redLed.toggle()
            utime.sleep_ms(20)
            for j in range (20):
                buzzer.toggle()
                #changed this time to make the buzzer on/off more apparent
                utime.sleep_ms(20)
        alarming = False
    elif pin == pir2:
        print("Alarm! Motion detected in Zone 2!!")
        alarming = True
        for i in range (10):
            grnLed.toggle()
            utime.sleep_ms(20)
            for j in range (20):
                buzzer.toggle()
                #changed this time to make the buzzer on/off more apparent
                utime.sleep_ms(20)
        alarming = False
    else:
        print("This should never happen :)")
    print("Alarm ended!")

pir1.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
pir2.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

grnLed.on()

while not alarming:
    print("Alarm active, no motion detected.")
    for i in range(10):
        redLed.toggle()
        grnLed.toggle()
        utime.sleep(1)
