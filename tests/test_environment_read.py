"""
Test Script for Environmental Sensors

Tests reading from DHT22 temperature/humidity sensor and LDR photoresistor.

Hardware Required:
- DHT22 sensor on GPIO 22
- LDR photoresistor on GPIO 26 (ADC0)

Author: TODO: Your name
Date: TODO: Date
"""

from machine import Pin, ADC
import dht
import time

def test_dht22():
    """Test DHT22 temperature and humidity readings."""
    print("\n=== Testing DHT22 Sensor ===")
    print("Reading temperature and humidity (5 times)...")
    
    sensor = dht.DHT22(Pin(22))
    
    for i in range(5):
        try:
            sensor.measure()
            temp = sensor.temperature()
            humidity = sensor.humidity()
            
            print(f"  Reading {i+1}:")
            print(f"    Temperature: {temp}°C")
            print(f"    Humidity: {humidity}%")
            
            time.sleep(2)
        except OSError as e:
            print(f"!    Reading {i+1} failed: {e}")
            time.sleep(2)
    
    print(" DHT22 test complete!")


def test_ldr():
    """Test LDR light level readings."""
    print("\n=== Testing LDR Sensor ===")
    print("Reading light levels (5 times)...")
    print("Try covering/uncovering the sensor...")
    
    ldr = ADC(Pin(26))
    
    for i in range(5):
        # Read raw ADC value
        raw_value = ldr.read_u16()
        
        # Convert to 0-1000 scale
        light_level = int((raw_value / 65535) * 1000)
        
        # Determine brightness
        if light_level < 200:
            brightness = "Bright"
        elif light_level < 500:
            brightness = "Medium"
        else:
            brightness = "Dark"
        
        print(f"  Reading {i+1}:")
        print(f"    Raw value: {raw_value}")
        print(f"    Light level: {light_level}")
        print(f"    Brightness: {brightness}")
        
        time.sleep(2)
    
    print(" LDR test complete!")


def test_both_sensors():
    """Test reading both sensors together."""
    print("\n=== Testing Both Sensors Together ===")
    print("Reading all environmental data (5 times)...")
    
    dht_sensor = dht.DHT22(Pin(22))
    ldr = ADC(Pin(26))
    
    for i in range(5):
        print(f"\nReading {i+1}:")
        
        # Read temperature/humidity
        try:
            dht_sensor.measure()
            temp = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            print(f"  Temperature: {temp}°C")
            print(f"  Humidity: {humidity}%")
        except OSError as e:
            print(f"!    DHT22 error: {e}")
        
        # Read light level
        raw_value = ldr.read_u16()
        light_level = int((raw_value / 65535) * 1000)
        print(f"  Light level: {light_level}")
        
        time.sleep(2)
    
    print("\n Combined sensor test complete!")


if __name__ == "__main__":
    print("=" * 50)
    print("  ENVIRONMENTAL SENSOR TEST SUITE")
    print("=" * 50)
    
    try:
        test_dht22()
        time.sleep(1)
        
        test_ldr()
        time.sleep(1)
        
        test_both_sensors()
        
        print("\n" + "=" * 50)
        print("  ALL TESTS COMPLETE!")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n\n  Tests interrupted by user")
