from machine import Pin
import time

laser = Pin(16, Pin.OUT)

number = [4,6,2,0,1,5,0,8]

while True:
    for num in number:
        
        if num == 0:
            num = 10
            
        for i in range(num):
            laser.value(1)
            time.sleep(0.065)
            laser.value(0)        
            time.sleep(0.035)
            
        time.sleep(0.1)
    time.sleep(5)	
