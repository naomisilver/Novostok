import time
import board
import digitalio
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from hid_gamepad import Gamepad
import usb_hid


# setup ADS1115
i2c = busio.I2C(scl=board.GP27, sda=board.GP26)
ads = ADS.ADS1115(i2c)
ads.gain = 1

# analogue joystick inputs from ADS1115
left_x = AnalogIn(ads, ADS.P1)   # A1
left_y = AnalogIn(ads, ADS.P0)   # A0
right_x = AnalogIn(ads, ADS.P3)  # A3
right_y = AnalogIn(ads, ADS.P2)  # A2

button_pins = {
    "rt": board.GP13,
    "rb": board.GP12,
    "lt": board.GP11,
    "lb": board.GP10,
    "dpad_up": board.GP21,
    "dpad_down": board.GP18,
    "dpad_left": board.GP19,
    "dpad_right": board.GP20,
    "start": board.GP9,
    "select": board.GP8,
    "a": board.GP3,
    "b": board.GP5,
    "x": board.GP4,
    "y": board.GP6,
    "l_stick_btn": board.GP7,
    "r_stick_btn": board.GP2,
}

buttons = {}
for name, pin in button_pins.items():
    btn = digitalio.DigitalInOut(pin)
    btn.switch_to_input(pull=digitalio.Pull.UP)
    buttons[name] = btn

# init gamepad
gp = Gamepad(usb_hid.devices)

# constants for joystick scaling
JOY_CENTER = 32768
JOY_RANGE = 32768
JOY_DEADZONE = 3000

def scale_axis(val):
    delta = val - JOY_CENTER
    if abs(delta) < JOY_DEADZONE:
        return 0
    return max(-127, min(127, int((delta / JOY_RANGE) * 127)))

while True:
    lx = scale_axis(left_x.value)
    ly = -scale_axis(left_y.value)
    rx = scale_axis(right_x.value)
    ry = -scale_axis(right_y.value)
    gp.move_joysticks(x=lx, y=ly, z=rx, r_z=ry)

    for i, (name, btn) in enumerate(buttons.items()):
        if not btn.value:
            gp.press_buttons(i + 1)
        else:
            gp.release_buttons(i + 1)

    time.sleep(0.01)
