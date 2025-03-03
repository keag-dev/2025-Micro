import machine
import utime

pir1 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)

redLed = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(13, machine.Pin.OUT)

def pir_handler(pin):
    print("Alarm! Motion detected!!")
    for i in range (10):
        redLed.toggle()
        utime.sleep_ms(20)
        for j in range (20):
            buzzer.toggle()
            utime.sleep_ms(2)

pir1.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    redLed.toggle()
    utime.sleep(2)