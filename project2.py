from machine import Pin, Timer
from machine import Pin,PWM
from time import sleep
#import RPi.GPIO as GPIO
import time
led = Pin(25, Pin.OUT)
timer = Timer()
print("Please wait...")

def blink(timer):
    led.toggle()
pwm_pins = [16]
pwms = [PWM(Pin(pwm_pins[0]))]
[pwm.freq(1000) for pwm in pwms]
step_val = 64
range_0 = [ii for ii in range(0,2**16,step_val)]
range_1 = [ii for ii in range(2**16,-step_val,-step_val)]
print("Please wait some more...")

#start of state one

timer.init(freq=1, mode=Timer.PERIODIC, callback=blink)
for i in range (0, 19):
    for pwm in pwms: 
           for ii in range_0+range_1:
               pwm.duty_u16(ii)
               time.sleep(0.001)
x = 'spongebob squarepants'
guess = input("Who lives in a pineapple under the sea (lower case): ")
while guess != x:
    print("oops try again")
    guess = input("Who lives in a pineapple under the sea (lower case): ")
print("Moving to the next part. Please wait!")

for i in range (0, 3):
    for pwm in pwms: 
           for ii in range_0+range_1:
               pwm.duty_u16(ii)
               time.sleep(0.001)
y = 'fsh'
guess = input("What do you call a fish with no eyes?")
while guess != y:
    print("oops guess again")
    guess = input("What do you call a fish with no eyes?")
print("Good job, please wait for next stage")

#start of stage two

print("Please wait some more...")

timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)
for i in range (0, 15):
    for pwm in pwms: 
           for ii in range_0+range_1:
               pwm.duty_u16(ii)
               time.sleep(0.001)
z = 'no'
guess = input("Do you like this style of puzzle?:")
while guess != z:
    print("really?")
    guess = input("Do you like this style of puzzle?:")
print("Okay good, you're not supposed to enjoy this")

for i in range (0, 20):
    for pwm in pwms:
        for ii in range_0+range_1:
            pwm.duty_u16(ii)
            time.sleep(0.001)

print("Okay, get ready:")
a = 'please send help'
guess = input("01010111 01101111 01110111 00101100 00100000 01111001 01101111 01110101 00100000 01110010 01100101 01100001 01101100 01101100 01111001 00100000 01100110 01101001 01100111 01110101 01110010 01100101 01100100 00100000 01110100 01101000 01101001 01110011 00100000 01101111 01110101 01110100 00101110 00100000 01001001 00100000 01100111 01110101 01100101 01110011 01110011 00100000 01111001 01101111 01110101 00100111 01110010 01100101 00100000 01101110 01101111 01110100 00100000 01110100 01101000 01100001 01110100 00100000 01100100 01110101 01101101 01100010 00100000 01100001 01100110 01110100 01100101 01110010 01100001 01101100 01101100 00101110:")
while guess != a:
    print("ASCII/UTF-8 ?")
    guess = input("Letter: ")
print("Hey congrats you googled an ascii to text converter. Please wait for next stage.")

#start of stage three

timer.init(freq=3, mode=Timer.PERIODIC, callback=blink)
for i in range (0, 20):
    for pwm in pwms:
        for ii in range_0+range_1:
            pwm.duty_u16(ii)
            time.sleep(0.001)
#print("Geez, be patient")
b = 'pico'
guess = input("What's the name of the microcontroller you're using right now?:")
while guess != b:
    print("huh?")
    guess = input("What's the name of the microcontroller you're using right now?: ")
print("Congratualations! Solved!")
timer.init(freq=10, mode=Timer.PERIODIC, callback=blink)

#solved State
print('PUZZLE SOLVED! Secret Key: 6c00e6ff6ea6bcc6ac122ec314eb16749ca88f03760adfb71a9de657527c6396')
