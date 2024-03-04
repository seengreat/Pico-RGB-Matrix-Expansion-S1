from machine import Pin, ADC
import neopixel
import time

LDR = ADC(26)

strip=neopixel.NeoPixel()
strip.pixels_fill(strip.BLUE)
while True:
    # martix brightens with ambient brightness
    #strip.brightness = 0.7*(1-LDR.read_u16()/65535)

    # martix darkens with ambient brightness
    strip.brightness = LDR.read_u16()/65536
    #strip.brightness = 0.1
#     print(LDR.read_u16())
    strip.pixels_show()   