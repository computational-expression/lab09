"""
Mock DHT module for testing Lab 09 on regular Python.
Simulates DHT22 sensor behavior.
"""

class DHT22:
    """Mock DHT22 temperature and humidity sensor."""
    
    def __init__(self, pin):
        """Initialize DHT22 sensor on a pin."""
        self.pin = pin
        self._temperature = 22.5  # Default temperature in Celsius
        self._humidity = 55.0     # Default humidity percentage
        self._should_error = False
    
    def measure(self):
        """Trigger a measurement (simulated)."""
        if self._should_error:
            raise OSError("Sensor read failed")
        # In real sensor, this triggers reading
        pass
    
    def temperature(self):
        """Return the last measured temperature."""
        return self._temperature
    
    def humidity(self):
        """Return the last measured humidity."""
        return self._humidity
    
    def set_values(self, temp, humidity):
        """Set sensor values for testing."""
        self._temperature = temp
        self._humidity = humidity
    
    def set_error(self, should_error):
        """Set whether sensor should raise an error."""
        self._should_error = should_error
