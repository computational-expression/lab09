"""
Environment Sensor Module
TODO: Complete this class to manage environmental sensor readings from DHT22.
"""
from machine import Pin
import dht
import time


class EnvironmentSensor:
    """Tracks temperature and humidity with alert detection."""
    
    def __init__(self, location, temp_pin):
        """
        TODO: Initialize sensor with location name and pin number.
        - Set self.location to the location parameter
        - Initialize self.reading_history as an empty list
        - Create self.dht_sensor using dht.DHT22(Pin(temp_pin))
        """
        pass  # TODO: Replace with your code
    
    def read_conditions(self):
        """
        TODO: Read all environmental conditions and return as dictionary.
        - Use try/except to handle OSError from sensor
        - Call self.dht_sensor.measure()
        - Get temp = self.dht_sensor.temperature()
        - Get humidity = self.dht_sensor.humidity()
        - If OSError, set temp and humidity to 0.0
        - Get current time using time.localtime()
        - Format timestamp as "HH:MM:SS"
        - Return dictionary with keys: 'location', 'temperature', 'humidity', 'timestamp'
        """
        pass  # TODO: Replace with your code
    
    def add_to_history(self, reading):
        """
        TODO: Add reading to history, keeping only last 10 readings.
        - Append reading to self.reading_history
        - If length > 10, keep only last 10 using slice [-10:]
        """
        pass  # TODO: Replace with your code
    
    def get_average_temp(self):
        """
        TODO: Calculate average temperature from reading history.
        - If reading_history is empty, return 0.0
        - Initialize total = 0
        - Loop through each reading in self.reading_history
        - Add reading['temperature'] to total
        - Return total / len(self.reading_history)
        """
        pass  # TODO: Replace with your code
    
    def get_status_summary(self):
        """
        TODO: Generate human-readable summary of current conditions.
        - Call self.read_conditions() and store in variable conditions
        - Categorize temperature: <18="Cold", <=26="Comfortable", else="Warm"
        - Categorize humidity: <30="Dry", <=60="Comfortable", else="Humid"
        - Return formatted string with location, temp (C), humidity (%), and time
        """
        pass  # TODO: Replace with your code
    
    def check_alerts(self):
        """
        TODO: Check for environmental alert conditions.
        - Call self.read_conditions() and store in variable conditions
        - Set high_temp = True if temperature > 28, else False
        - Set low_temp = True if temperature < 16, else False
        - Set high_humidity = True if humidity > 70, else False
        - Return dictionary with keys: 'high_temp', 'low_temp', 'high_humidity', 'any_alerts'
        - 'any_alerts' should be True if ANY of the three alerts are True
        """
        pass  # TODO: Replace with your code


if __name__ == "__main__":
    # Test your implementation
    sensor = EnvironmentSensor("TEST_LAB", 2)
    conditions = sensor.read_conditions()
    print(f"Temp: {conditions['temperature']}C")
    print(sensor.get_status_summary())
    
    # Test alerts
    alerts = sensor.check_alerts()
    print("ALERTS" if alerts['any_alerts'] else "Normal")
