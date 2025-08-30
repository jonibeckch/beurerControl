#!/usr/bin/env python3
import time
from tl100 import TL100Lamp
def main():
 lamp = TL100Lamp()
 print("Verbinde mit Beurer TL100 Lampe...")
 lamp.start_solar_mode()
 print("Tageslichtmodus aktiv. 30 Sekunden warten...")
 time.sleep(30)
 lamp.start_color_mode()
 print("Farbmodus aktiv - Farbe: Gelb (FFFF00), Helligkeit: 50%")
 lamp.set_color("FFFF00")
 lamp.set_color_brightness(50)
 time.sleep(10)
 lamp.stop_color_mode()
 lamp.stop_solar_mode()
 print("Lampe ausgeschaltet.")
if __name__ == "__main__":
    main()