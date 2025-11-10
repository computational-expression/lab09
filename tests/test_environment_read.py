"""
Test Script for Environmen            print(f"    Temperature: {temp}C")
            print(f"    Humidity: {humidity}%")l Sensors

Tests reading from DHT22 temperature/humidity sensor.

Hardware Required:
- DHT22 sensor on GPIO 2

Author: TODO: Your name
Date: TODO: Date
"""

from machine import Pin
import dht
import time

def test_dht22():
    """Test DHT22 temperature and humidity readings."""
    print("\n=== Testing DHT22 Sensor ===")
    print("Reading temperature and humidity (5 times)...")
    
    sensor = dht.DHT22(Pin(2))
    
    for i in range(5):
        try:
            sensor.measure()
            temp = sensor.temperature()
            humidity = sensor.humidity()
            
            print(f"  Reading {i+1}:")
            print(f"    Temperature: {temp} C")
            print(f"    Humidity: {humidity}%")
            
            time.sleep(2)
        except OSError as e:
            print(f"  [!] Reading {i+1} failed: {e}")
            time.sleep(2)
    
    print("[OK] DHT22 test complete!")


if __name__ == "__main__":
    print("=" * 50)
    print("  ENVIRONMENTAL SENSOR TEST SUITE")
    print("=" * 50)
    
    try:
        test_dht22()
        
        print("\n" + "=" * 50)
        print("  ALL TESTS COMPLETE!")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n\n[!] Tests interrupted by user")
