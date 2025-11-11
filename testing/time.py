"""
Mock time module for testing - uses regular Python time but adds MicroPython compatibility.
"""

import time as _time

# Re-export standard time functions
sleep = _time.sleep
time = _time.time
localtime = _time.localtime

# Add MicroPython-specific functions
def sleep_ms(milliseconds):
    """Sleep for specified milliseconds (MicroPython compatibility)."""
    _time.sleep(milliseconds / 1000.0)

def ticks_ms():
    """Return millisecond counter (MicroPython compatibility)."""
    return int(_time.time() * 1000)

def ticks_diff(ticks1, ticks2):
    """Calculate difference between ticks (MicroPython compatibility)."""
    return ticks1 - ticks2
