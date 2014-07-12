#! /usr/bin/env python
"""
    allows pressing of a 'trigger key' to create an always-on effect
    on a 'target key' 
"""

import win32api
import win32con
import time

TRIGGER_KEY = 6
TARGET_KEY = 5

if __name__ == "__main__":
    done = False
    while not done:
        # we'll read our trigger key to see if we should toggle
        win32api.keybd_event(win32con.SHIFT_PRESSED, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
