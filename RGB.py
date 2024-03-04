import neopixel
import time

strip=neopixel.NeoPixel()
strip.brightness=0.2

while True:
    for i in range (10):
        strip.pixels_fill(strip.COLORS[i])
        time.sleep(0.5)
        strip.pixels_show()
    strip.rainbow_cycle(0.1)