from machine import Pin
import dht
import time


class EnvironmentSensor:
    
    def __init__(self, location, temp_pin):
        # TODO: Initialize sensor with location name and GPIO pin number
        # TODO: Create empty reading_history list to store sensor readings
        # TODO: Initialize DHT22 sensor object using the temp_pin
        pass
    
    def read_conditions(self):
        # TODO: Read temperature and humidity from DHT22 sensor
        # TODO: Handle sensor errors with try-except (OSError)
        
        # Get current time
        current_time = time.localtime()
        hours = current_time[3]
        minutes = current_time[4]
        seconds = current_time[5]
        timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
        # TODO: Return dictionary with location, temperature, humidity, and timestamp
        pass
    
    def add_to_history(self):
        # TODO: Add a sensor reading dictionary to the reading_history list
        # TODO: Keep only the last 10 readings (limit history size)
        pass
    
    def get_average_temp(self):
        # TODO: Calculate and return the average temperature from reading_history
        # TODO: Return 0.0 if history is empty
        pass
    
    def get_status_summary(self):
        # TODO: Read current conditions and create a summary string
        # TODO: Include location, temperature, humidity, and categorization (Cold/Comfortable/Warm, Dry/Comfortable/Humid)
        # TODO: Return formatted string with current time
        pass
    
    def check_alerts(self):
        # TODO: Read current conditions and check for alert thresholds
        # TODO: Check if temperature is too high (>28C) or too low (<16C)
        # TODO: Check if humidity is too high (>70%)
        # TODO: Return dictionary with high_temp, low_temp, high_humidity, and any_alerts flags
        pass


if __name__ == "__main__":
    # Test your implementation
    sensor = EnvironmentSensor("TEST_LAB", 2)
    print(sensor.read_conditions())
    print(sensor.get_status_summary())
    print(sensor.check_alerts())

