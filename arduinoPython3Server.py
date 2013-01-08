#! /usr/bin/env python3
#arduinoPython3Server.py 
""" 
Simple single-threaded server that allows the lights to be switched on and off
using client software
"""

import socket
import serial
import time
import sys

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

#Helper methods to encode and decode the data
def toString(data):
   return data.decode('utf-8')

def toBytes(data):
   return bytes(data,'utf-8')

HOST = '192.168.0.5'          # Symbolic name
PORT = 6000     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server started")

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

data=conn.recv(1024)
conn.send(toBytes("Welcome Client"))
print ("Connected by", addr)
print(toString(data))


while True:
    data = conn.recv(1024)
    if (data.decode('utf-8'))=='q':
        print("server closing")
        n='0'
        arduino.write(n.encode('utf-8'))
        arduino.close()
        break

    else:
        print("I got ",data.decode('utf-8'))
        arduino.write(data)
    
conn.close()
s.close()


