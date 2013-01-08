#! /usr/bin/env python3
import serial
import time
import sys
from tkinter import *


'''Need to call Tk() so that BooleanVar can be initialised and set
http://tinyurl.com/b94wzmj
Setting this to false initially.
This code needs to be improved so that all on switches all check boxes on and
all off state switches off all check boxes
'''

Tk()
allOn = BooleanVar()
allOn.set(False)

#Define the parameters of the serial port

try:
    arduino = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
        )
except:
    print("port not found")
    sys.exit()

'''function to control lights.
This needs to be re-written so that the lights check boxes are monitored
before any action is taken'''

def light(inp):
    if inp==4 and allOn.get()==False:
        inp = 4
        allOn.set(True)      
        
    elif inp==4 and allOn.get() == True:
        inp =0
        allOn.set(False)


    
    try:
        number = str(inp)
        arduino.write(number.encode('utf-8'))
        
    except:
        print("failed")

'''function exits cleanly by switching off lights and closing serial port'''
def endConnection():
    n='0'
    arduino.write(n.encode('utf-8'))
    arduino.close()
    print('you have quit')
    frame.quit()



frame = Frame()
frame.pack()
Label(frame, text='Main Window').pack(side=TOP)

Checkbutton(frame, text='Green', command =lambda:light(1)).pack(side=LEFT)
Checkbutton(frame, text='Red', command =lambda:light(2)).pack(side=LEFT)
Checkbutton(frame, text='Yellow', command =lambda:light(3)).pack(side=LEFT)
Checkbutton(frame, text='All on', command =lambda:light(4)).pack(side=LEFT)

Button(frame, text='Quit',command = endConnection,).pack(side=RIGHT)

frame.mainloop()
