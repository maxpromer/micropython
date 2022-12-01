from machine import Pin
import display
import buzzer

Pin(25, Pin.OUT).value(0)
Pin(27, Pin.OUT).value(0)
Pin(28, Pin.OUT).value(0)
Pin(29, Pin.OUT).value(0)
display.clear()
buzzer.off()
