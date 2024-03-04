Pico RGB Matrix Expansion S1 from seengreat:www.seengreat.com
 =======================================
# Instructions
## Product Overview
The Pico RGB Matrix Expansion S1 is an expansion board designed specifically for the Raspberry Pi Pico. It features a 10x20 WS2812 RGB LED matrix, DS1302 real-time clock chip, analog silicon microphone audio sampling circuit, light-dependent resistor, and reset button.<br>

## Product Parameters
|Dimensions	|79.5mm (length) * 39.8mm (width) * 11mm (height)|
|----------------------|--------------------------------------------------------|
|Power Supply Voltage	|5V (Powered by Pico)|
|LED Matrix Resolution	|10 * 20 (pixels)|
|RGB LED Color	|24-bit (8 bits per color)|
|RGB LED Communication Method	|Single-wire data transmission|
|RGB LED Brightness Levels	|256 levels of brightness|
|RGB LED Data Transfer Rate	|800Kbps/second|
|RTC Chip	|DS1302ZM|
|Microphone Pre-amplifier Chip	|MCP6022I/SN|
|Microphone Sensitivity	|-32db|
|Microphone Frequency Response	|100~10000hz|
|Microphone Output Signal	|Analog|

## Product Dimensions
|Dimensions	|79.5mm (length) * 39.8mm (width) * 11mm (height)|
|----------------------|--------------------------------------------------------|
|Mounting Hole Diameter	|3mm|
|Weight	|22.5g|
# Usage 
## Resource Introduction and Pin Definitions
The module resources are as shown in the following diagram:<br>
![image](https://github.com/seengreat/Pico-RGB-Matrix-Expansion-S1/blob/main/1.png)<br>
![image](https://github.com/seengreat/Pico-RGB-Matrix-Expansion-S1/blob/main/2.png)<br>
Figure 2-1 Pico RGB Matrix Expansion S1 Resource Introduction Diagram<br>
①CR1220 Button Battery Holder<br>         
②Raspberry Pi Pico Female Header<br>              
③Light-Dependent Resistor Connector  <br>               
④DS1302 Real-Time Clock Chip    <br>        
⑤Raspberry Pi Pico Reset Button<br>	 
⑥Analog Silicon Microphone<br>
⑦Silicon Microphone Amplification Adjustment<br>
⑧WS2812 RGB Matrix screen Interface Connector<br>
⑨0807 RGB LED Matrix screen<br>
	
![image](https://github.com/seengreat/Pico-RGB-Matrix-Expansion-S1/blob/main/3.png)<br>
Figure 2-2 Pico RGB Matrix Expansion S1 Pinout Diagram<br>
                         
WS2812 RGB LED Matrix: Controlled via the GP22 pin of the Raspberry Pi Pico, and the expansion board's bottom has a PH2.0 1*4-pin connector that can be used to connect other control devices to control the LED matrix screen. It can display various texts and simple patterns. This screen is of the RGB type, with each pixel composed of 3 LED lights(red, green, blue), capable of displaying rich colors and diverse effects. Suitable for data display, dynamic display, music rhythm display, and other applications.<br>

DS1302 Real-Time Clock Chip: Controlled via the GP6, GP7, GP8 (RST, IO, SCLK) pins of the Raspberry Pi Pico. This chip is powered primarily by the Raspberry Pi Pico, with a button cell battery on the expansion board providing backup power, enabling timing even when the Raspberry Pi Pico is not powered. This circuit can also display the time on the LED matrix, forming a simple electronic clock.<br>

Analog Silicon Microphone Audio Sampling Circuit: This circuit is powered by the Raspberry Pi Pico and has high sensitivity, capable of capturing faint sounds. It outputs analog signals to the GP28 pin, allowing for music rhythm display on the LED matrix when combined with the Raspberry Pi Pico.<br>

Light-Dependent Resistor: The expansion board also features a PH2.0 connector for inserting a light-dependent resistor. After inserting the light-dependent resistor, the board can sense changes in ambient light. This is a type of sensor; when the ambient light changes, the resistance of the resistor itself changes, decreasing with brightness. It outputs corresponding voltage changes, allowing for brightness control of the expansion board through programming.<br>

Reset Button: The Raspberry Pi Pico lacks a reset button. This product adds a reset button so that users can reset or debug without frequently plugging and unplugging the Pico's USB cable.<br>

## Using Python Examples
1.Install Thonny<br>
Thonny download link: https://thonny.org<br>
2.After installing Thonny, with the Pico powered off, press and hold the BOOTSEL button on the Pico, then connect it to your computer via USB. Release the button, and a RPI-RP2 disk directory will pop up. Drag the micropython-firmware-Pico-w-130623.uf2 file from the Pico RGB Matrix Expansion S1 directory into the RPI-RP2 disk.<br>
<br>
3.Right-click on DS1302.py under the Pico RGB Matrix Expansion S1 directory and open it with Thonny. Click on Tools -> Options. In the interpreter field, select MicroPython (Raspberry Pi Pico), and set the port (COMx: the port number may vary on different computers). Click OK to confirm.<br>
①Select "MicroPython (Raspberry Pi Pico)".<br>
②Set the corresponding port, and click OK to confirm.<br>
<br>
4.Open the View -> Files window, and upload the Lib library files to the Raspberry Pi Pico.<br>
①Press Ctrl and select all .py files inside the Pico RGB Matrix Expansion S1 folder.<br>
②Click "Upload to /" to save these files to the Raspberry Pi Pico.<br>
<br>
5.Open the prepared RGB.py file, then click the "Run current script" button or press the F5 key to run the current script. Observe the display on the LED matrix.<br>
<br>
6.Insert the prepared button battery into the battery holder, open the RTC.py script, then click the "Run current script" button or press the F5 key to run the current script. Observe the display on the LED matrix.<br>
①Click "Run current script" to run the example program.<br>
②Observe whether the time display in the shell window is correct.<br>
③Check if the time displayed in the shell window matches the set time.<br>
<br>
Install the button battery on the expansion board, comment out the code for setting the time, and observe whether the timing function works properly after power off. If the time continues to increase as originally set, it indicates that the button battery is supplying power normally.<br>
①Comment out the code :"DS1302.SetTime(23,9,7,23,59,59,00,4)".<br>
②Click "Run current script" to run the example program.<br>
③Observe whether the time in the shell window continues to increase before and after power off.<br>
<br>
7.Open the fft.py script, then click the "Run current script" button or press the F5 key to run the current script. Generate some noise or play some music, and observe the LED matrix on the expansion board. The LEDs on the LED matrix correspond from left to right to low frequency to high frequency. See if the lights on the LED matrix rhythmically change with the sound.<br>
① Click  "Run current script" to run the example program.<br>
<br>
8.Insert the light-dependent resistor into the female header labeled "LDR" on the expansion board.<br>
Open the LDR.py script, then click the "Run current script" button or press the F5 key to run the current script. Illuminate or place the light-dependent resistor in a dark place as appropriate, and observe whether the LED matrix brightens or dims with changes in ambient light.<br>
<br>
9.Press the reset button on the side of the expansion board and observe whether the expansion board resets successfully.<br>
