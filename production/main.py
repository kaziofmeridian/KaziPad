import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
# For Rotary Encoder
from kmk.modules import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
# For OLED
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306


keyboard = KMKKeyboard()
Encoder_handler = EncoderHandler()
keyboard.modules.append(Layers())

# 3x3 matrix of keys
keyboard.col_pins = (board.D3, board.D10, board.D9)
keyboard.row_pins = (board.D0,board.D1, board.D2)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# rotary encoder
Encoder_handler.pins = ((board.D5, board.D4, board.D8)) # (left, right, pressed)

keyboard.modules.append(Encoder_handler)
keyboard.extensions.append(MediaKeys())

# toggle layer with encoder button press

LAYER_TOGGLE = KC.TG(1)
Encoder_handler.map = ((KC.VOLU, KC.VOLD, LAYER_TOGGLE))

# 3x3 matrix of Keys
keyboard.keymap = [
    [# Layer: 0 - Base Layer / Shortcuts
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.CTL(KC.X),
     KC.LCTL(KC.A), KC.LCTL(KC.F), KC.LCTL(KC.Z),
     KC.LEFT, KC.UP, KC.RIGHT],
     [# Layer: 1 - Numpad
        KC.N7, KC.N8, KC.N9,
     KC.N4, KC.N5, KC.N6,
     KC.N1, KC.N2, KC.N3],
]

#OLED screen
display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    width=128,
    height=32,
    flip = False,
    entries = [
        TextEntry = (text='Kazipad - Base', x=0, y=0, layer=0), # Only displays on layer 0
        TextEntry = (text='Kazipad - Numpad', x=0, y=0, layer=1)# Only displays on layer 1
    ],
)
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()