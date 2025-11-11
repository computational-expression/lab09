"""
Test suite for EnvironmentSensor class.
Tests sensor reading, history management, and alert detection.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))

# Import mock modules first
import machine
import dht
import time

# Now import the student's code
from src.environment_sensor import EnvironmentSensor


def test_initialization():
    """Test that sensor initializes correctly."""
    print("Testing EnvironmentSensor initialization...")
    
    sensor = EnvironmentSensor("Lab Room", 2)
    
    # Check that location is stored
    assert hasattr(sensor, 'location'), "Sensor should have location attribute"
    assert sensor.location == "Lab Room", "Location should be 'Lab Room'"
    
    # Check that reading_history exists and is empty
    assert hasattr(sensor, 'reading_history'), "Sensor should have reading_history attribute"
    assert isinstance(sensor.reading_history, list), "reading_history should be a list"
    assert len(sensor.reading_history) == 0, "reading_history should start empty"
    
    # Check that DHT sensor is created
    assert hasattr(sensor, 'dht_sensor'), "Sensor should have dht_sensor attribute"
    
    print("✓ Initialization test passed!")


def test_read_conditions():
    """Test reading sensor conditions."""
    print("\nTesting read_conditions method...")
    
    sensor = EnvironmentSensor("Test Lab", 2)
    
    # Set mock sensor values
    sensor.dht_sensor.set_values(25.0, 60.0)
    
    conditions = sensor.read_conditions()
    
    # Check return type
    assert isinstance(conditions, dict), "read_conditions should return a dictionary"
    
    # Check required keys
    required_keys = ['location', 'temperature', 'humidity', 'timestamp']
    for key in required_keys:
        assert key in conditions, f"Dictionary should contain '{key}' key"
    
    # Check values
    assert conditions['location'] == "Test Lab", "Location should match"
    assert conditions['temperature'] == 25.0, "Temperature should be 25.0"
    assert conditions['humidity'] == 60.0, "Humidity should be 60.0"
    assert ':' in conditions['timestamp'], "Timestamp should contain ':'"
    
    print("✓ read_conditions test passed!")


def test_add_to_history():
    """Test adding readings to history."""
    print("\nTesting add_to_history method...")
    
    sensor = EnvironmentSensor("History Test", 2)
    
    # Add a few readings
    reading1 = {'temperature': 20.0, 'humidity': 50.0, 'timestamp': '10:00:00'}
    reading2 = {'temperature': 22.0, 'humidity': 55.0, 'timestamp': '10:01:00'}
    
    sensor.add_to_history(reading1)
    assert len(sensor.reading_history) == 1, "History should have 1 reading"
    
    sensor.add_to_history(reading2)
    assert len(sensor.reading_history) == 2, "History should have 2 readings"
    
    # Test that history is limited to 10 readings
    for i in range(15):
        sensor.add_to_history({'temperature': 20 + i, 'humidity': 50 + i, 'timestamp': f'10:{i:02d}:00'})
    
    assert len(sensor.reading_history) <= 10, "History should be limited to 10 readings"
    
    print("✓ add_to_history test passed!")


def test_get_average_temp():
    """Test calculating average temperature."""
    print("\nTesting get_average_temp method...")
    
    sensor = EnvironmentSensor("Avg Test", 2)
    
    # Test with empty history
    avg = sensor.get_average_temp()
    assert avg == 0.0, "Average should be 0.0 for empty history"
    
    # Add readings
    sensor.add_to_history({'temperature': 20.0, 'humidity': 50.0})
    sensor.add_to_history({'temperature': 24.0, 'humidity': 55.0})
    sensor.add_to_history({'temperature': 22.0, 'humidity': 60.0})
    
    avg = sensor.get_average_temp()
    expected = (20.0 + 24.0 + 22.0) / 3
    assert abs(avg - expected) < 0.01, f"Average should be {expected}, got {avg}"
    
    print("✓ get_average_temp test passed!")


def test_check_alerts():
    """Test alert detection."""
    print("\nTesting check_alerts method...")
    
    sensor = EnvironmentSensor("Alert Test", 2)
    
    # Test normal conditions (no alerts)
    sensor.dht_sensor.set_values(22.0, 50.0)
    alerts = sensor.check_alerts()
    
    assert isinstance(alerts, dict), "check_alerts should return a dictionary"
    assert 'high_temp' in alerts, "Should have high_temp key"
    assert 'low_temp' in alerts, "Should have low_temp key"
    assert 'high_humidity' in alerts, "Should have high_humidity key"
    assert 'any_alerts' in alerts, "Should have any_alerts key"
    
    assert alerts['high_temp'] == False, "No high temp alert at 22C"
    assert alerts['low_temp'] == False, "No low temp alert at 22C"
    assert alerts['high_humidity'] == False, "No high humidity alert at 50%"
    assert alerts['any_alerts'] == False, "No alerts should be active"
    
    # Test high temperature alert
    sensor.dht_sensor.set_values(30.0, 50.0)
    alerts = sensor.check_alerts()
    assert alerts['high_temp'] == True, "High temp alert should be active at 30C"
    assert alerts['any_alerts'] == True, "any_alerts should be True"
    
    # Test low temperature alert
    sensor.dht_sensor.set_values(14.0, 50.0)
    alerts = sensor.check_alerts()
    assert alerts['low_temp'] == True, "Low temp alert should be active at 14C"
    assert alerts['any_alerts'] == True, "any_alerts should be True"
    
    # Test high humidity alert
    sensor.dht_sensor.set_values(22.0, 75.0)
    alerts = sensor.check_alerts()
    assert alerts['high_humidity'] == True, "High humidity alert should be active at 75%"
    assert alerts['any_alerts'] == True, "any_alerts should be True"
    
    print("✓ check_alerts test passed!")


def test_get_status_summary():
    """Test status summary generation."""
    print("\nTesting get_status_summary method...")
    
    sensor = EnvironmentSensor("Summary Test", 2)
    
    # Set known values
    sensor.dht_sensor.set_values(22.5, 55.0)
    
    # Get summary
    summary = sensor.get_status_summary()
    
    # Check that it returns a string
    assert isinstance(summary, str), "get_status_summary should return a string"
    
    # Check that it contains expected information
    assert "Summary Test" in summary, "Summary should contain location"
    assert "22.5" in summary or "22" in summary, "Summary should contain temperature"
    assert "55" in summary, "Summary should contain humidity"
    
    print("✓ get_status_summary test passed!")


def run_all_tests():
    """Run all test functions."""
    print("=" * 60)
    print("Running EnvironmentSensor Tests")
    print("=" * 60)
    
    try:
        test_initialization()
        test_read_conditions()
        test_add_to_history()
        test_get_average_temp()
        test_check_alerts()
        test_get_status_summary()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
