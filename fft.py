import math
import time
import neopixel

# bit reverse perform bit reversal operation
# x: is an integer that represents the target number for the bit reversal operation.
# n: is an integer that represents the number of bits in "x"
def bit_reverse(x, n):
    result = 0
    for i in range(n):
        if (x >> i) & 1:
            result |= 1 << (n - 1 - i)
    return result

# fft Fast Fourier Transform
# a:input a list of powers of 2 in length for FFT
def fft(a):
    n = len(a)
    log2n = int(math.log2(n))
    a = [a[bit_reverse(i, log2n)] for i in range(n)]
    for s in range(1, log2n + 1):
        m = 1 << s
        wm = complex(math.cos(2 * math.pi / m), math.sin(2 * math.pi / m))
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * a[k + j + m // 2]
                u = a[k + j]
                a[k + j] = u + t
                a[k + j + m // 2] = u - t
                w *= wm
    return a

#Initialize the pin for ADC Sample
potentiometer = machine.ADC(28)
#Initialize NeoPixel
strip=neopixel.NeoPixel()
strip.brightness=0.2

# Sample rate  
# Because the frequency used for demonstration noise is generally low, the sample rate is set to 1k  
# If you measure the voice of a person speaking, set it to about 10k here 
fs = 10000

tim2 = machine.Timer()  # For ADC sampling 

fftin = [0 for i in range(0, 64, 1)]    # The data used to calculate the spectrum, here do 64 numbers of FFT
fftbuff = [0 for i in range(0, 64, 1)]  # For display spectrum
adcbuff = [0 for i in range(0, 1000, 1)]# The 16-bit voltage sampled by the ADC is directly stored here.

k=0

# Collect 120 numbers as a group
def adc_sample(Pin):
    global adcbuff
    global k
    if k < 120:  
        adcbuff[k] = potentiometer.read_u16()
        k = k+1

tim2.init(freq=fs, mode=machine.Timer.PERIODIC, callback=adc_sample)



while True:
    if k >= 120:
        for i in range(0, 64, 1):
            # The division by 30000 here is for the convenience of waveform processing and has no practical meaning
            fftin[i] = ((adcbuff[i]-33500)/30000*1)
        fftbuff = fft(fftin)
        for i in range(0, 32, 1):
            if int(abs(fftbuff[i])) <1:
                fftbuff[i]=1
            fftbuff[i] = (int)(20*math.log10(abs(fftbuff[i])))  # Integer, easy to draw lines

            if fftbuff[i]>10:  # Prevent overflow
                fftbuff[i]=10
        
        for i in range(20):
            strip.drow_line(i,fftbuff[i+3])
        strip.pixels_show()
        strip.pixels_fill(strip.BLACK)
        k = 0  # Re-enable ADC sampling