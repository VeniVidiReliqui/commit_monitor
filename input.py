#!/usr/bin/env python3
'''
Button manager for Unicorn MiniHat.
'''
from gpiozero import Button
from time import sleep

button_name_map = {5: "A",
              6: "B",
              16: "X",
              24: "Y"}

class BtnEnum:
    BTN_A = 0
    BTN_B = 1
    BTN_X = 2
    BTN_Y = 3
    BTN_NUM = 4

class ButtonManager:
    """Manager for buttons on Unicorn MiniHat"""
    def __init__(self):
        """Initialize fixed buttons on Unicorn MiniHat"""
        button_a = Button(5)
        button_b = Button(6)
        button_x = Button(16)
        button_y = Button(24)
        self._b_arr = [
            button_a,
            button_b,
            button_x,
            button_y]

    def __enter__(self):
        """Handle instantiation using 'with' keyword."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Handle cleanup when going out of scope."""
        for btn in self._b_arr:
            btn.close()

    def set_btn_pressed_cb(self, btn_index, cb_fn):
        """Set pressed callback for specified button.
        
        Callback takes button object as an argument.
        """
        if (btn_index < BtnEnum.BTN_NUM and btn_index >= 0):
            self._b_arr[btn_index].when_pressed = cb_fn

    def set_btn_held_cb(self, btn_index, cb_fn):
        """Set held callback for specified button.
        
        Callback takes button object as an argument.
        """
        if (btn_index < BtnEnum.BTN_NUM and btn_index >= 0):
            self._b_arr[btn_index].when_held = cb_fn

    def set_btn_released_cb(self, btn_index, cb_fn):
        """Set released callback for specified button.
        
        Callback takes button object as an argument.
        """
        if (btn_index < BtnEnum.BTN_NUM and btn_index >= 0):
            self._b_arr[btn_index].when_released = cb_fn


def pressed(button):
    button_name = button_name_map[button.pin.number]
    print(f"Button {button_name} pressed")


def held(button):
    button_name = button_name_map[button.pin.number]
    print(f"Button {button_name} held")


def released(button):
    button_name = button_name_map[button.pin.number]
    print(f"Button {button_name} released")


if __name__ == "__main__":
    try:
        with ButtonManager() as bm:
            bm.set_btn_pressed_cb(BtnEnum.BTN_A, pressed)
            bm.set_btn_pressed_cb(BtnEnum.BTN_B, pressed)
            bm.set_btn_pressed_cb(BtnEnum.BTN_X, pressed)
            bm.set_btn_pressed_cb(BtnEnum.BTN_Y, pressed)

            bm.set_btn_held_cb(BtnEnum.BTN_A, held)
            bm.set_btn_held_cb(BtnEnum.BTN_B, held)
            bm.set_btn_held_cb(BtnEnum.BTN_X, held)
            bm.set_btn_held_cb(BtnEnum.BTN_Y, held)

            bm.set_btn_released_cb(BtnEnum.BTN_A, released)
            bm.set_btn_released_cb(BtnEnum.BTN_B, released)
            bm.set_btn_released_cb(BtnEnum.BTN_X, released)
            bm.set_btn_released_cb(BtnEnum.BTN_Y, released)

            print("Ready.")
            while(True):
                sleep(0.1)

    except KeyboardInterrupt:
        print("Done.")
