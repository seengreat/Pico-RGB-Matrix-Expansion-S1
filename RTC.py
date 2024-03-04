import neopixel
import DS1302
import time
# The pins occupied by DS1302
SCLK = 8   # GP8
IO = 7     # GP7
RST = 6    # GP6
# Initialize DS1302
DS1302=DS1302.DS1302(SCLK,IO,RST)
DS1302.SetTime(23,9,7,23,59,00,4)

# Initialize NeoPixel matrix screen
strip = neopixel.NeoPixel()
strip.brightness = 0.2
time = DS1302.GetTime() # (year,month,day,hour,minute,second,week)
time_last = time
strip.martix_show_week(time[6],strip.CYAN,strip.BLUE)
Week = ['Mon.','Tue.','Wed.','Thu.','Fri.','Sat.','Sun.']
# Display hour, minute and week in main loop
while True:
    time=DS1302.GetTime()
    today = int(time[6])
    if (time_last[6] != time[6]):
        strip.martix_show_week(today,strip.CYAN,strip.BLUE)
    if (time_last != time):
        strip.martix_show_time(4,time[3],time[4],strip.CYAN)
        time_last = time
        hour = "{:02d}".format(time[3])
        minute = "{:02d}".format(time[4])
        sec = "{:02d}".format(time[5])
        print('\n\n\nDate:20{}-{}-{}\nTime:{}:{}:{}\nWeekday:{}\n\n'.format(time[0],time[1],time[2],hour,minute,sec,Week[today-1]))