#! /usr/bin/env python3
'''Client for arduinoPython3Server.py GUI client that connects to the 
server and then allows lights to be controlled. Proof of concept of 
client server methods for controlling the Arduino '''

import serial
import time
import sys
import socket
from tkinter import *



def toString(data):
   return data.decode('utf-8')

def toBytes(data):
   return bytes(data,'utf-8')



HOST = '192.168.0.5'       # The remote host
PORT = 6000                # Port used by the server
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((HOST, PORT))
except:
   print("no server")
   sys.exit()
   
s.send(toBytes("I am the Python client"))

data=s.recv(1024)
print(toString(data))





'''Need to call Tk() so that BooleanVar can be initialised and set
http://tinyurl.com/b94wzmj
Setting this to false initially.
This code needs to be improved so that all on switches all check boxes on and
all off state switches off all check boxes
'''

Tk()
allOn = BooleanVar()
allOn.set(False)



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
    d =str(inp)
    print(d," Sent to server")
    s.send(toBytes(d))



    


'''function exits cleanly by switching off lights and closing serial port'''
def endConnection():
    s.send(toBytes("q"))
    s.close()
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
