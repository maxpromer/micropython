from machine import Pin, ADC

A0 = const(0)
A1 = const(1)
A2 = const(2)
A3 = const(3)
A4 = const(4)
A5 = const(5)
A6 = const(6)
A7 = const(7)

MUX_CH0 = Pin(22, Pin.OUT)
MUX_CH1 = Pin(23, Pin.OUT)
MUX_CH2 = Pin(24, Pin.OUT)

ADC = ADC(Pin(26))
mux_map_ch = [[0,1,0],[1,0,0],[0,0,0],[1,1,0],[0,0,1],[0,1,1],[1,1,1],[1,0,1]]

def mux_select(pin):
    MUX_CH0.value(mux_map_ch[pin][0])
    MUX_CH1.value(mux_map_ch[pin][1])
    MUX_CH2.value(mux_map_ch[pin][2])

def analog_read(pin):
    mux_select(pin)
    return ADC.read_u16() >> 4

def analog_read_calibrated(pin):
    return min(max(analog_read(pin) - 24, 0), 4000)
