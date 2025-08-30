# beurerControl
A simple python script to control the Beurer Daylight Lamp, based on the Repository https://github.com/Deadolus/ha-beurer which was built the control a beurer Lamp with the home assiant

Step 1 - Install bleak:
```pip install bleak```


Coding:
from bleak import BleakClient, BleakScanner, BLEDevice, BleakGATTCharacteristic, BleakError
BleakScanner.discover()


Current status: Not working
Tried plenty of different devices (Mac, Raspberry), nevertheless I could never figure out which commands had to be sent, so it didn't work so far.
