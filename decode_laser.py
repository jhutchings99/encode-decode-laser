from machine import Pin
import time

button = Pin(17, Pin.IN, Pin.PULL_UP)

pulses = 0
digits = []

pulse_timeout = 100
valid_pulse = 70

print_time = time.ticks_ms()
printed = True

while True:
    if not button.value():
        # start counting pulses
        pulse_start = time.ticks_ms()
        pulses = 0
        while not button.value():
            pass
        pulse_end = time.ticks_ms()

        # check if pulse is valid
        if pulse_end - pulse_start > valid_pulse:
            print("Adding pulse")
            pulses += 1

        # loop while pulse hasnt reached timeout
        while time.ticks_ms() - pulse_end < pulse_timeout:
            if not button.value():
                # detected another valid pulse
                pulse_start = time.ticks_ms()
                while not button.value():
                    pass
                pulse_end = time.ticks_ms()
                if pulse_end - pulse_start > valid_pulse:
                    print("Adding pulse")
                    pulses += 1

        if pulses == 10:
            digits.append(0)
        elif pulses > 0:
            digits.append(pulses)
            
        printed = False
        print_time = time.ticks_ms()
        
    if time.ticks_ms() - print_time > 3000 and not printed:
        printed = True
        new_str = ""
        for num in digits:
            new_str += str(num)
        new_str += "\n"
        print(new_str)
