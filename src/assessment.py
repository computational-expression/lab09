"""
Assessment Script for Lab 09
Tests the EnvironmentSensor and DashboardController classes for correctness.
"""
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_environment_sensor():
    """Test EnvironmentSensor class methods and attributes."""
    try:
        from environment_sensor import EnvironmentSensor
        
        # Test 1: Object creation
        sensor = EnvironmentSensor("TEST_LAB", 22, 26)
        if sensor.location != "TEST_LAB":
            return False, "EnvironmentSensor location attribute incorrect"
        
        # Test 2: Check reading_history is a list
        if not isinstance(sensor.reading_history, list):
            return False, "EnvironmentSensor reading_history must be a list"
        
        # Test 3: Check reading_history starts empty
        if len(sensor.reading_history) != 0:
            return False, "EnvironmentSensor reading_history should start empty"
        
        # Test 4: Test add_to_history method
        test_reading = {
            'location': 'TEST_LAB',
            'temperature': 22.5,
            'humidity': 45.0,
            'light_level': 300,
            'timestamp': '12:00:00'
        }
        sensor.add_to_history(test_reading)
        if len(sensor.reading_history) != 1:
            return False, "EnvironmentSensor add_to_history not working"
        
        # Test 5: Test history keeps only 10 readings
        for i in range(15):
            sensor.add_to_history(test_reading)
        if len(sensor.reading_history) != 10:
            return False, "EnvironmentSensor reading_history should keep only 10 readings"
        
        # Test 6: Test get_average_temp with data
        sensor.reading_history = []
        sensor.add_to_history({'temperature': 20.0})
        sensor.add_to_history({'temperature': 22.0})
        sensor.add_to_history({'temperature': 24.0})
        avg = sensor.get_average_temp()
        if not (21.9 < avg < 22.1):  # Allow small floating point variance
            return False, "EnvironmentSensor get_average_temp calculation incorrect"
        
        # Test 7: Test get_average_temp with empty history
        sensor.reading_history = []
        avg = sensor.get_average_temp()
        if avg != 0.0:
            return False, "EnvironmentSensor get_average_temp should return 0.0 for empty history"
        
        return True, "EnvironmentSensor tests passed"
        
    except Exception as e:
        return False, f"EnvironmentSensor error: {str(e)}"


def test_dashboard_controller():
    """Test DashboardController class methods and attributes."""
    try:
        from dashboard_controller import DashboardController
        
        # Test 1: Object creation
        dashboard = DashboardController(15, 14)
        
        # Test 2: Check display_mode initialization
        if dashboard.display_mode != "temperature":
            return False, "DashboardController display_mode should initialize to 'temperature'"
        
        # Test 3: Check button_press_count initialization
        if dashboard.button_press_count != 0:
            return False, "DashboardController button_press_count should initialize to 0"
        
        # Test 4: Check mode_history is a list
        if not isinstance(dashboard.mode_history, list):
            return False, "DashboardController mode_history must be a list"
        
        # Test 5: Check mode_history starts empty
        if len(dashboard.mode_history) != 0:
            return False, "DashboardController mode_history should start empty"
        
        # Test 6: Test cycle_display_mode changes mode
        initial_mode = dashboard.display_mode
        dashboard.cycle_display_mode()
        if dashboard.display_mode == initial_mode:
            return False, "DashboardController cycle_display_mode should change mode"
        
        # Test 7: Test button_press_count increments
        if dashboard.button_press_count != 1:
            return False, "DashboardController cycle_display_mode should increment button_press_count"
        
        # Test 8: Test mode_history tracks changes
        if len(dashboard.mode_history) != 1:
            return False, "DashboardController cycle_display_mode should add to mode_history"
        
        # Test 9: Test mode cycling order
        dashboard2 = DashboardController(15, 14)
        modes_cycled = []
        for _ in range(4):
            dashboard2.cycle_display_mode()
            modes_cycled.append(dashboard2.display_mode)
        expected_order = ["light", "alerts", "history", "temperature"]
        if modes_cycled != expected_order:
            return False, "DashboardController modes should cycle: temperature → light → alerts → history"
        
        # Test 10: Test get_mode_stats returns correct structure
        stats = dashboard.get_mode_stats()
        if not isinstance(stats, dict):
            return False, "DashboardController get_mode_stats should return a dictionary"
        if 'current_mode' not in stats:
            return False, "DashboardController get_mode_stats should include 'current_mode'"
        if 'button_presses' not in stats:
            return False, "DashboardController get_mode_stats should include 'button_presses'"
        if 'mode_counts' not in stats:
            return False, "DashboardController get_mode_stats should include 'mode_counts'"
        
        # Test 11: Test reset_stats
        dashboard.reset_stats()
        if dashboard.button_press_count != 0:
            return False, "DashboardController reset_stats should reset button_press_count to 0"
        if len(dashboard.mode_history) != 0:
            return False, "DashboardController reset_stats should clear mode_history"
        
        # Test 12: Test get_mode_display_title returns string
        title = dashboard.get_mode_display_title()
        if not isinstance(title, str):
            return False, "DashboardController get_mode_display_title should return a string"
        if len(title) == 0:
            return False, "DashboardController get_mode_display_title should return non-empty string"
        
        return True, "DashboardController tests passed"
        
    except Exception as e:
        return False, f"DashboardController error: {str(e)}"


def main():
    """Run all assessment tests."""
    print("=" * 60)
    print("Lab 09 Assessment - Testing Classes")
    print("=" * 60)
    
    all_passed = True
    
    # Test EnvironmentSensor
    print("\nTesting EnvironmentSensor class...")
    sensor_passed, sensor_msg = test_environment_sensor()
    print(f"  Result: {sensor_msg}")
    all_passed = all_passed and sensor_passed
    
    # Test DashboardController
    print("\nTesting DashboardController class...")
    dashboard_passed, dashboard_msg = test_dashboard_controller()
    print(f"  Result: {dashboard_msg}")
    all_passed = all_passed and dashboard_passed
    
    # Final result
    print("\n" + "=" * 60)
    if all_passed:
        print("ASSESSMENT RESULT: All tests passed / True")
    else:
        print("ASSESSMENT RESULT: Some tests failed / False")
    print("=" * 60)
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
