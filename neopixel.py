# Example using PIO to drive a set of WS2812 LEDs.
import array, time
from machine import Pin
import rp2
import random
from font import num_font
# import DS1302
# from font import num_font
# Configure the number of WS2812 LEDs.
NUM_LEDS = 200
# Set the control pin of neopixel
PIN_NUM = 22
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()
        
class NeoPixel(object):
    def __init__(self,pin=PIN_NUM,num=NUM_LEDS,brightness=0.1):
        self.pin=pin
        self.num=num
        self.brightness = brightness
        
        # Create the StateMachine with the ws2812 program, outputting on pin
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)

        self.ar = array.array("I", [0 for _ in range(self.num)])
        
        self.BLACK = (0, 0, 0)
        self.RED = (15, 0, 0)
        self.ORINGE = (15,5,0)
        self.YELLOW = (5,15,0)
        self.GREEN = (0, 15, 0)
        self.CYAN = (0,15,5)
        self.GB = (0,5,15)
        self.BLUE = (0, 0, 15)
        self.INDIGO = (5,0,15)
        self.PURPLE = (15,0,5)
        
        self.WHITE = (15, 15, 15)
        self.COLORS = [self.RED, self.ORINGE, self.YELLOW,self.GREEN, self.CYAN,self.GB, self.BLUE,self.INDIGO,self.PURPLE,self.RED]
        self.LINE =[[0,20,40,60,80,100,120,140,160,180,0],
                    [1,21,41,61,81,101,121,141,161,181,1],
                    [2,22,42,62,82,102,122,142,162,182,2],
                    [3,23,43,63,83,103,123,143,163,183,3],
                    [4,24,44,64,84,104,124,144,164,184,4],
                    [5,25,45,65,85,105,125,145,165,185,5],
                    [6,26,46,66,86,106,126,146,166,186,6],
                    [7,27,47,67,87,107,127,147,167,187,7],
                    [8,28,48,68,88,108,128,148,168,188,8],
                    [9,29,49,69,89,109,129,149,169,189,9],
                    [10,30,50,70,90,110,130,150,170,190,10],
                    [11,31,51,71,91,111,131,151,171,191,11],
                    [12,32,52,72,92,112,132,152,172,192,12],
                    [13,33,53,73,93,113,133,153,173,193,13],
                    [14,34,54,74,94,114,134,154,174,194,14],
                    [15,35,55,75,95,115,135,155,175,195,15],
                    [16,36,56,76,96,116,136,156,176,196,16],
                    [17,37,57,77,97,117,137,157,177,197,17],
                    [18,38,58,78,98,118,138,158,178,198,18],
                    [19,39,59,79,99,119,139,159,179,199,19]]
        
    ##########################################################################
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.num)])
        for i,c in enumerate(self.ar):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        self.sm.put(dimmer_ar, 8)

    def pixels_set(self, i, color):
        self.ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

    def pixels_fill(self, color):
        for i in range(len(self.ar)):
            self.pixels_set(i, color)

    # The colours are a transition r - g - b - back to r.
    # pos:Input a value 0 to 31 to get a color value.
    def wheel(self, pos):
        if pos < 0 or pos > 31:
            return (0, 0, 0)
        if pos < 10:
            return (31 - pos * 3, pos * 3, 0)
        if pos < 15:
            pos -= 10
            return (0, 31 - pos * 3,pos * 3)
        pos -= 15
        return (pos * 3, 0, 31 - pos * 3)
     
    # Drow a vertical line
    # line_n: the entered number controls which columns are lit , 0~19
    # height: the height of this line
    def drow_line (self,line_n,height):
        for i in range (height):
            self.pixels_set(self.LINE[line_n][i],self.COLORS[i])
    
    # Drow a vertical black line, used to erase the last displayed vertical line
    # line_n: the entered number controls which columns are lit , 0~19
    # height: the height of this line
    def drow_line_black (self,line_n,height):
        for i in range (height,-1,-1):
            self.pixels_set(self.LINE[line_n][i],self.BLACK)

    # Display a single number
    # x: x is the column where the first pixel is located
    # y: y is the row where the first pixel is located
    # num: num is the number to be displayed 0~9
    # color: the color of numbers
    def drow_single_num (self,x,y,num,color): #4*5
        for i in range(5):
            for j in range(4):
                if num_font[num][i][j]:
                    self.pixels_set(20*(4-i+y)+j+x,color)
                else :
                    self.pixels_set(20*(4-i+y)+j+x,self.BLACK)
        self.pixels_show()
    
    # martix show the hour and minute
    # y: y is the row where the time is located
    # hour: input the hour and display
    # minute: input the minute and display
    # color: the color of time
    def martix_show_time (self,y,hour,minute,color):
        self.drow_single_num (1,y,int(hour/10),color)     
        self.drow_single_num (5,y,hour%10,color) 
        self.drow_single_num (12,y,int(minute//10),color)
        self.drow_single_num (16,y,minute%10,color)
        self.drow_single_num (8,y,10,color)
        time.sleep(0.5)
        self.drow_single_num (8,y,11,color)
        time.sleep(0.5)
        
    # martix show the week
    # week: input the week and display
    # color: color of the week
    # b_color: color of the other days of the week 
    def martix_show_week(self,week,color,b_color):
        for i in range(7):
            if ((week-1)==i):
                self.pixels_set(i*3,color)
                self.pixels_set(1+i*3,color)
                self.pixels_set(20+i*3,color)
                self.pixels_set(21+i*3,color)
            else:
                self.pixels_set(i*3,b_color)
                self.pixels_set(1+i*3,b_color)
                self.pixels_set(20+i*3,b_color)
                self.pixels_set(21+i*3,b_color)
            
    # martix show rainbow cycle
    # wait: rainbow cycle wait time
    def rainbow_cycle(self, wait):
        for j in range(256):
            for i in range(self.num):
                rc_index = (i * 256 // self.num) + j
                self.pixels_set(i, self.wheel(rc_index & 31))
            self.pixels_show()
            time.sleep(wait)
            
            
            
            
            