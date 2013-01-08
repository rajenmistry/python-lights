python-lights
=============

Interfacing with Arduino with Python. These are primarily 
proof-of-concept projects that were developed in Python to assess the 
feasibility of interfacing before developing more in Java.

arduinoPython3GUI.py
--------------------

Python3 script that uses check boxes to control the lights on an Arduino 
board. This was written as a proof of concept. Numbers 1-4 control the lights.

arduinoPython3Server.py
-----------------------

Python3 script that runs a single-threaded server to allow a client to 
connect and then control lights on the board

arduinoPythonClientGUI.py
-------------------------

Python3 script that runs a GUI client that connects to the server above 
and allows the lights to be controlled


_120616_lightController.ino
---------------------------

Program running on the Arduino to control the lights that are attached 
to the board

