"""
Environment Sensor Module - STARTER

Your task: Complete the EnvironmentSensor class methods.
"""
from machine import Pin, ADC
import dht
import time


class EnvironmentSensor:
    """Manages environmental sensor readings from DHT22 and LDR."""
    
    def __init__(self, location, temp_pin, light_pin):
        """Initialize with location name and sensor pins."""
        # TODO: Store location, temp_pin, light_pin as instance variables
        # TODO: Initialize reading_history as empty list
        # TODO: Create DHT22 sensor object on temp_pin
        # TODO: Create ADC object on light_pin for LDR
        pass
    
    # TODO: Add read_temperature(self) method
    # Read from DHT22, return dict with temperature, humidity, success, error
    
    # TODO: Add read_light(self) method
    # Read ADC value from LDR, convert to 0-1000 scale, return int
    
    # TODO: Add read_conditions(self) method
    # Read all sensors, create timestamp, return dict with all data
    
    # TODO: Add add_to_history(self, reading) method
    # Append reading to history, keep only last 10 readings
    
    # TODO: Add get_average_temp(self) method
    # Calculate and return average temperature from history
    
    # TODO: Add get_status_summary(self) method
    # Read conditions, categorize temp/humidity/light, return formatted string
    
    # TODO: Add check_alerts(self) method
    # Check for alert conditions, return dict with alert flags


if __name__ == "__main__":
    # Test environment sensor
    sensor = EnvironmentSensor("TEST_LAB", 22, 26)
    conditions = sensor.read_conditions()
    print(f"Temp: {conditions['temperature']}°C")
    print(sensor.get_status_summary())
    
    # Test alerts
    alerts = sensor.check_alerts()
    print("ALERTS" if alerts['any_alerts'] else "Normal")
