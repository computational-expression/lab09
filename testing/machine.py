"""
Mock machine module for testing Lab 09 on regular Python.
This allows tests to run without MicroPython hardware dependencies.
"""

class Pin:
    """Mock Pin class that simulates MicroPython Pin behavior."""
    
    # Pin modes
    IN = "IN"
    OUT = "OUT"
    
    # Pull resistor options
    PULL_UP = "PULL_UP"
    PULL_DOWN = "PULL_DOWN"
    
    def __init__(self, pin_number, mode=None, pull=None):
        """Initialize a mock pin."""
        self.pin_number = pin_number
        self.mode = mode
        self.pull = pull
        self._value = 1 if pull == Pin.PULL_UP else 0
        self._state = False
    
    def on(self):
        """Turn the pin on (for output pins)."""
        if self.mode == Pin.OUT:
            self._state = True
    
    def off(self):
        """Turn the pin off (for output pins)."""
        if self.mode == Pin.OUT:
            self._state = False
    
    def value(self, val=None):
        """Get or set the pin value."""
        if val is not None:
            self._value = val
            return None
        return 1 if self._state else self._value


class PWM:
    """Mock PWM class for buzzer control."""
    
    def __init__(self, pin):
        """Initialize PWM on a pin."""
        self.pin = pin
        self._freq = 0
        self._duty = 0
    
    def freq(self, frequency=None):
        """Get or set PWM frequency."""
        if frequency is not None:
            self._freq = frequency
        return self._freq
    
    def duty_u16(self, duty=None):
        """Get or set PWM duty cycle (16-bit)."""
        if duty is not None:
            self._duty = duty
        return self._duty
