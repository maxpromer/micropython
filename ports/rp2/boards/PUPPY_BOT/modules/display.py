import ili9341
from machine import Pin, PWM, SPI

spi = SPI(0, 10_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16)) # MISO is dumy pin
disp = ili9341.Display(spi, cs=Pin(17), dc=Pin(20), rst=Pin(21), width=160, height=128, rotation=270)

def color_hex(c):
    if type(c) is str:
        c = int(c[1:], 16)
    r = (c >> 16) & 0xFF
    g = (c >> 8) & 0xFF
    b = c & 0xFF
    return ili9341.color565(b, g, r)

def clear():
    disp.clear(0)

def text(text, x, y, color, font):
    if font == "text8x8":
        disp.draw_text8x8(x, y, text, color_hex(color))
    else:
        disp.draw_text(x, y, text, font, color_hex(color))

def line(x1, y1, x2, y2, color):
    disp.draw_line(x1, y1, x2, y2, color_hex(color))

def fill_rect(x, y, width, height, color):
    disp.fill_rectangle(x, y, width, height, color_hex(color))

def rect(x, y, width, height, color):
    disp.draw_rectangle(x, y, width, height, color_hex(color))
    
def fill_circle(x, y, r, color):
    disp.fill_circle(x, y, r, color_hex(color))

def circle(x, y, r, color):
    disp.draw_circle(x, y, r, color_hex(color))

def fill(color):
    disp.clear(color_hex(color))

def image(data, x, y):
    width = (data[0] << 8) | data[1]
    height = (data[2] << 8) | data[3]
    disp.block(x, y, x + width - 1, y + height - 1, data[4:])
