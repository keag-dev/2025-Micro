import machine
import utime

pir1 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
pir2 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_DOWN)

redLed = machine.Pin(15, machine.Pin.OUT)
grnLed = machine.Pin(14, machine.Pin.OUT)
buzzer = machine.Pin(13, machine.Pin.OUT)

while True:
    timer_start = utime.ticks_ms()
    redLed.off()
    grnLed.off()
    buzzer.off()

    while pir1.value() == True:
        redLed.on()
        buzzer.on()
        delay_time = utime.ticks_diff(utime.ticks_ms(), timer_start)
        #the example is wrong here, rather than calculating the delay again,
        #we just use the one we calculated on the previous line. doing the
        #calculaton again just leads to printing a slightly incorrect value
        print("PIR 1 time delay set to " + str(delay_time) + "ms")
        utime.sleep(0.1)

    while pir2.value() == True:
        grnLed.on()
        delay_time = utime.ticks_diff(utime.ticks_ms(), timer_start)
        #same as above, idk why they chose to do it like this :/
        print("PIR 2 time delay set to " + str(delay_time) + "ms")
        utime.sleep(0.1)