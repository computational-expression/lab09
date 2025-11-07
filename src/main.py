"""
Environmental Monitoring Dashboard - STARTER
Demonstrates OOP with MULTIPLE sensor objects monitoring different locations.
"""
import time
from environment_sensor import EnvironmentSensor
from dashboard_controller import DashboardController


def display_mode_info(dashboard, sensors):
    """Display information based on current mode for ALL sensors."""
    print(dashboard.get_mode_display_title())
    
    for sensor in sensors:
        conditions = sensor.read_conditions()
        sensor.add_to_history(conditions)
        
        if dashboard.display_mode == "temperature":
            print(f"  {conditions['location']}: {conditions['temperature']:.1f}°C, "
                  f"{conditions['humidity']:.1f}%")
        
        elif dashboard.display_mode == "light":
            if conditions['light_level'] < 200:
                brightness = "Bright"
            elif conditions['light_level'] <= 500:
                brightness = "Medium"
            else:
                brightness = "Dark"
            print(f"  {conditions['location']}: {conditions['light_level']} ({brightness})")
        
        elif dashboard.display_mode == "alerts":
            alerts = sensor.check_alerts()
            if alerts['any_alerts']:
                alert_list = []
                if alerts['high_temp']: alert_list.append("Hot")
                if alerts['low_temp']: alert_list.append("Cold")
                if alerts['high_humidity']: alert_list.append("Humid")
                if alerts['low_light']: alert_list.append("Dark")
                print(f"  [!] {conditions['location']}: {', '.join(alert_list)}")
            else:
                print(f"  [OK] {conditions['location']}: Normal")
        
        elif dashboard.display_mode == "history":
            avg = sensor.get_average_temp()
            count = len(sensor.reading_history)
            print(f"  {conditions['location']}: Avg {avg:.1f}°C ({count} readings)")


def main():
    """Main monitoring loop with MULTIPLE sensor objects."""
    print("=" * 60)
    print("  MULTI-LOCATION ENVIRONMENTAL MONITORING DASHBOARD")
    print("=" * 60)
    print("\nInitializing hardware...")
    
    # TODO: Create MULTIPLE sensor objects - demonstrating OOP concept!
    # TODO: Each object is independent with its own location and history
    # TODO: Create a list called 'sensors' with at least 3 EnvironmentSensor objects
    # TODO: Use different location names like "LAB_A", "LAB_B", "OFFICE"
    # TODO: All sensors use the same hardware pins: temp_pin=22, light_pin=26
    # Hint: sensors = [EnvironmentSensor(...), EnvironmentSensor(...), ...]
    
    # Create single dashboard controller
    dashboard = DashboardController(15, 14)
    
    print(f"[OK] Initialized {len(sensors)} sensor objects!")
    print("  Each sensor maintains its own location and history.")
    print("\nPress button to cycle: Temperature → Light → Alerts → History")
    print("-" * 60)
    
    button_was_pressed = False
    reading_count = 0
    
    try:
        while True:
            # Button handling
            button_pressed = dashboard.read_button()
            if button_pressed and not button_was_pressed:
                dashboard.cycle_display_mode()
                print(f"\n[Switched to {dashboard.display_mode.upper()} mode]")
                button_was_pressed = True
            elif not button_pressed:
                button_was_pressed = False
            
            # Display data from all sensors
            reading_count += 1
            current_time = time.localtime()
            hours = current_time[3]
            minutes = current_time[4]
            seconds = current_time[5]
            print(f"\n[Reading #{reading_count}] - {hours:02d}:{minutes:02d}:{seconds:02d}")
            display_mode_info(dashboard, sensors)
            
            # Check for any alerts across all sensors
            any_sensor_alert = False
            for s in sensors:
                if s.check_alerts()['any_alerts']:
                    any_sensor_alert = True
                    break
            dashboard.indicate_alert({'any_alerts': any_sensor_alert})
            
            # Show statistics every 10 readings
            if reading_count % 10 == 0:
                stats = dashboard.get_mode_stats()
                print(f"\n[Stats] {stats['button_presses']} button presses, "
                      f"Modes: {stats['mode_counts']}")
            
            time.sleep(2)
    
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("  MONITORING STOPPED")
        print("=" * 60)
        
        # Show final summary for each sensor
        print(f"\nFinal Summary ({reading_count} readings):")
        for sensor in sensors:
            avg = sensor.get_average_temp()
            print(f"  {sensor.location}: Avg {avg:.1f}°C, "
                  f"{len(sensor.reading_history)} stored readings")
        
        stats = dashboard.get_mode_stats()
        print(f"\nDashboard: {stats['button_presses']} button presses")
        print(f"Mode usage: {stats['mode_counts']}")
        
        dashboard.set_led_state(False)
        print("\n[OK] Hardware cleaned up. Goodbye!")


if __name__ == "__main__":
    main()
