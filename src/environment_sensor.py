from machine import Pin
import dht
import time


class EnvironmentSensor:
    
    def __init__(self, location, temp_pin):
        # TODO: Initialize sensor with location name and GPIO pin number
        # TODO: Create empty reading_history list to store sensor readings
        # TODO: Initialize sensor object using the temp_pin
    
    def read_conditions(self):
        # Read temperature and humidity from sensor
        # Handle sensor errors with try-except (OSError)
        # Return dictionary with location, temperature, humidity, and timestamp
    
    def add_to_history(self, reading):
        # Add a sensor reading dictionary to the reading_history list
        # Keep only the last 10 readings (limit history size)
    
    def get_average_temp(self):
        # Calculate and return the average temperature from reading_history
        # Return 0.0 if history is empty
    
    def get_status_summary(self):
        # Read current conditions and create a summary string
        # Include location, temperature, humidity, and categorization
        # Return formatted string with current time
    
    def check_alerts(self):
        # Read current conditions and check for alert thresholds
        # Check if temperature is too high (>28C) or too low (<16C)
        # Check if humidity is too high (>70%)
        # Return dictionary with high_temp, low_temp, high_humidity, and any_alerts flags


if __name__ == "__main__":
    # Test your implementation
    sensor = EnvironmentSensor("TEST_LAB", 2)
    print(sensor.read_conditions())
    print(sensor.get_status_summary())
    print(sensor.check_alerts())


