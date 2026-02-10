import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners import DirectPins

# Initialize
keyboard = KMKKeyboard()

# 3-button matrix driven directly off GPIO
keyboard.matrix = DirectPins([
    board.D0,
    board.D1,
    board.D7,
])

# Knob
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D2, board.D3, board.D6, False),)
# Knob click toggles between layers
encoder_handler.map = [
    ((KC.MEDIA_VOLUME_UP, KC.MEDIA_VOLUME_DOWN, KC.TG(1)),),
    ((KC.MEDIA_VOLUME_UP, KC.MEDIA_VOLUME_DOWN, KC.TG(1)),),
]
keyboard.modules.append(encoder_handler)

# LEDs
rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=1,
    rgb_order='GRB'
)
keyboard.extensions.append(rgb)
keyboard.extensions.append(MediaKeys())

# Keymap
keyboard.keymap = [
    # Layer 0: Media Controls
    [KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK],
    
    # Layer 1: Copy/Pase/Undo
    [KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Z)],
]

if __name__ == '__main__':
    keyboard.go()
