"""
Environment Sensor Module

This module provides the EnvironmentSensor class for reading and tracking
temperature, humidity, and light conditions using DHT22 and LDR sensors.

Author: TODO: Your name
Date: TODO: Date
"""

# TODO: Import necessary libraries
# from machine import Pin, ADC
# import dht
# import time


class EnvironmentSensor:
    """
    Manages environmental sensor readings from DHT22 and LDR.
    
    Tracks temperature, humidity, and light levels over time and provides
    analysis of environmental conditions with alert detection.
    
    Attributes:
        location (str): Physical location identifier (e.g., "LAB_A")
        temp_pin (int): GPIO pin number for DHT22 sensor
        light_pin (int): GPIO pin number for LDR sensor (ADC)
        reading_history (list): List of dictionaries storing recent readings
    """
    
    def __init__(self, location, temp_pin, light_pin):
        """
        Initialize the EnvironmentSensor.
        
        Args:
            location (str): Location identifier (e.g., "LAB_A", "ROOM_101")
            temp_pin (int): GPIO pin for DHT22 temperature sensor
            light_pin (int): GPIO pin for LDR light sensor (must be ADC pin)
        
        Example:
            sensor = EnvironmentSensor("LAB_A", 22, 26)
        """
        # TODO: Store location as instance variable
        # TODO: Store pin numbers
        # TODO: Initialize reading_history as empty list
        # TODO: Set up DHT22 sensor on temp_pin
        # TODO: Set up ADC on light_pin for LDR
        pass
    
    def read_temperature(self):
        """
        Read temperature and humidity from DHT22 sensor.
        
        Returns:
            dict: Dictionary with keys 'temperature' (float), 'humidity' (float),
                  'success' (bool), and 'error' (str or None)
        
        Example:
            temp_data = sensor.read_temperature()
            if temp_data['success']:
                print(f"Temp: {temp_data['temperature']}°C")
        """
        # TODO: Try to measure from DHT22
        # TODO: If successful, return dictionary with temp and humidity
        # TODO: If error occurs, return dictionary with success=False and error message
        pass
    
    def read_light(self):
        """
        Read light level from LDR photoresistor.
        
        Returns:
            int: Light level value (0-1000 scale)
                 Higher values = darker, Lower values = brighter
        
        Example:
            light_level = sensor.read_light()
            print(f"Light: {light_level}")
        """
        # TODO: Read ADC value from LDR
        # TODO: Convert from 0-65535 to 0-1000 scale
        # TODO: Return converted value
        pass
    
    def read_conditions(self):
        """
        Read all environmental conditions (temperature, humidity, light).
        
        Returns:
            dict: Dictionary containing:
                - 'location' (str): Sensor location
                - 'temperature' (float): Temperature in Celsius
                - 'humidity' (float): Humidity percentage
                - 'light_level' (int): Light level (0-1000)
                - 'timestamp' (str): Reading timestamp
                - 'success' (bool): Whether reading was successful
        
        Example:
            conditions = sensor.read_conditions()
            print(f"Temp: {conditions['temperature']}°C")
            print(f"Light: {conditions['light_level']}")
        """
        # TODO: Call read_temperature() to get temp and humidity
        # TODO: Call read_light() to get light level
        # TODO: Get current timestamp
        # TODO: Combine all data into one dictionary
        # TODO: Include location and success status
        # TODO: Return complete conditions dictionary
        pass
    
    def add_to_history(self, reading):
        """
        Add a sensor reading to history, keeping only the last 10 readings.
        
        Args:
            reading (dict): Dictionary containing sensor reading data
        
        Example:
            conditions = sensor.read_conditions()
            sensor.add_to_history(conditions)
        """
        # TODO: Append reading to reading_history list
        # TODO: If list has more than 10 items, remove the oldest (first) item
        # Hint: Use list slicing to keep only last 10 items
        pass
    
    def get_average_temp(self):
        """
        Calculate average temperature from reading history.
        
        Returns:
            float: Average temperature, or 0.0 if no readings
        
        Example:
            avg = sensor.get_average_temp()
            print(f"Average temp: {avg:.1f}°C")
        """
        # TODO: If reading_history is empty, return 0.0
        # TODO: Use a loop to sum all temperature values from history
        # TODO: Divide sum by number of readings to get average
        # TODO: Return the average
        pass
    
    def get_status_summary(self):
        """
        Generate a human-readable summary of current environmental conditions.
        
        Returns:
            str: Multi-line string describing conditions
        
        Example:
            summary = sensor.get_status_summary()
            print(summary)
        """
        # TODO: Read current conditions
        # TODO: Determine temperature status (Cold < 18, Comfortable 18-26, Warm > 26)
        # TODO: Determine humidity status (Dry < 30, Comfortable 30-60, Humid > 60)
        # TODO: Determine brightness (Bright < 200, Medium 200-500, Dark > 500)
        # TODO: Format and return multi-line summary string
        pass
    
    def check_alerts(self):
        """
        Check for environmental alert conditions.
        
        Returns:
            dict: Dictionary with alert flags:
                - 'high_temp' (bool): Temperature > 28°C
                - 'low_temp' (bool): Temperature < 16°C
                - 'high_humidity' (bool): Humidity > 70%
                - 'low_light' (bool): Light level > 600 (too dark)
                - 'any_alerts' (bool): True if any alert is active
        
        Example:
            alerts = sensor.check_alerts()
            if alerts['any_alerts']:
                print("⚠️ Environmental alerts detected!")
        """
        # TODO: Read current conditions
        # TODO: Check if temperature > 28 (high_temp)
        # TODO: Check if temperature < 16 (low_temp)
        # TODO: Check if humidity > 70 (high_humidity)
        # TODO: Check if light level > 600 (low_light/too dark)
        # TODO: Determine if any alerts are active
        # TODO: Return dictionary with all alert flags
        pass


# Test code - only runs when this file is executed directly
if __name__ == "__main__":
    print("Testing EnvironmentSensor class...")
    
    # TODO: Create an EnvironmentSensor object
    # TODO: Read and print conditions
    # TODO: Add reading to history
    # TODO: Print status summary
    # TODO: Check and print alerts
    
    print("\nEnvironmentSensor test complete!")
