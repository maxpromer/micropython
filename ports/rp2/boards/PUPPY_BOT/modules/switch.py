# Dev by Sonthaya Nongnuch

from machine import Pin
import _thread
import utime

SW1 = Pin(6, Pin.IN, Pin.PULL_UP)

__sw1_press = None
__sw1_release = None

def __onSwitchChangesValue(pin):
    if pin.value():
        callback = None
        if pin == SW1:
            callback = __sw1_release
        if callback:
            # _thread.start_new_thread(callback, ())
            callback()
    else:
        callback = None
        if pin == SW1:
            callback = __sw1_press
        if callback:
            # _thread.start_new_thread(callback, ())
            callback()


# SW1.irq(handler=__onSwitchChangesValue, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)

def value(pin):
    return 0 if pin.value() else 1

def press(pin, callback):
    global __sw1_press, __sw2_press
    if pin == SW1:
        __sw1_press = callback

def release(pin, callback):
    global __sw1_release, __sw2_release
    if pin == SW1:
        __sw1_release = callback

__sw1_pressed = None

SW12 = 99

def SwitchLoopTask():
    sw1_press_start = None
    sw1_press_flag = False
    while True:
        sw1 = SW1.value()

        # S1
        if sw1 == 0: # S1 is press
            if sw1_press_start == None:
                sw1_press_start = utime.ticks_ms()
        else:
            if sw1_press_start != None:
                diff = utime.ticks_ms() - sw1_press_start
                if diff >= 40:
                    if __sw1_pressed:
                        __sw1_pressed()
                sw1_press_start = None
        
        utime.sleep_ms(20)
    

_thread.start_new_thread(SwitchLoopTask, ())

def pressed(pin, callback):
    global __sw1_pressed, __sw2_pressed, __sw12_pressed
    if pin == SW1:
        __sw1_pressed = callback
