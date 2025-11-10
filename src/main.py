"""
Environmental Monitoring Dashboard - SOLUTION
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
            print(f"  {conditions['location']}: {conditions['temperature']:.1f}C, "
                  f"{conditions['humidity']:.1f}%")
        
        elif dashboard.display_mode == "alerts":
            alerts = sensor.check_alerts()
            if alerts['any_alerts']:
                alert_list = []
                if alerts['high_temp']: alert_list.append("Hot")
                if alerts['low_temp']: alert_list.append("Cold")
                if alerts['high_humidity']: alert_list.append("Humid")
                print(f"  [!] {conditions['location']}: {', '.join(alert_list)}")
            else:
                print(f"  [OK] {conditions['location']}: Normal")
        
        elif dashboard.display_mode == "history":
            avg = sensor.get_average_temp()
            count = len(sensor.reading_history)
            print(f"  {conditions['location']}: Avg {avg:.1f}C ({count} readings)")


def main():
    """Main monitoring loop with MULTIPLE sensor objects."""
    print("=" * 60)
    print("  MULTI-LOCATION ENVIRONMENTAL MONITORING DASHBOARD")
    print("=" * 60)
    print("\nInitializing hardware...")
    
    # Create MULTIPLE sensor objects - demonstrating OOP concept!
    # Each object is independent with its own location and history
    sensors = [
        EnvironmentSensor("LAB_A", 2),  # Primary sensor
        EnvironmentSensor("LAB_B", 2),  # Same hardware, different location tracking
        EnvironmentSensor("OFFICE", 2)  # Another location
    ]
    
    # Create single dashboard controller
    dashboard = DashboardController(15, 16, 14)  # LED=15, Button=16, Buzzer=14
    
    print(f"[OK] Initialized {len(sensors)} sensor objects!")
    print("  Each sensor maintains its own location and history.")
    print("\n" + "=" * 60)
    print("HOW TO USE:")
    print("  - Press BUTTON to cycle display modes")
    print("  - Press Ctrl+C to quit")
    print("=" * 60)
    print(f"\nCurrent Mode: {dashboard.display_mode.upper()}")
    print("Mode Order: TEMPERATURE -> ALERTS -> HISTORY -> (repeat)")
    print("\nStarting in 3 seconds...")
    time.sleep(3)
    print("-" * 60)
    
    reading_count = 0
    last_button_state = False
    
    try:
        while True:
            # Take and display sensor readings
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
            
            # Activate LED and buzzer if there are alerts
            if any_sensor_alert:
                dashboard.indicate_alert({'any_alerts': True})
                print("  [!] ALERT ACTIVE - LED blinking, buzzer sounding")
            
            # Show statistics every 10 readings
            if reading_count % 10 == 0:
                stats = dashboard.get_mode_stats()
                print(f"\n[Statistics] {stats['button_presses']} button presses, "
                      f"Modes: {stats['mode_counts']}")
            
            # Wait 5 seconds, but check button frequently during wait
            print("\n[Press button to change mode]")
            for i in range(10):  # Check button 10 times over 5 seconds
                button_is_pressed = dashboard.read_button()
                
                # Detect button press (was not pressed, now pressed)
                if button_is_pressed and not last_button_state:
                    dashboard.cycle_display_mode()
                    print(f"\n{'*' * 60}")
                    print(f"  BUTTON PRESSED - Switched to {dashboard.display_mode.upper()} mode")
                    print(f"{'*' * 60}\n")
                
                last_button_state = button_is_pressed
                time.sleep(0.5)  # Check every 0.5 seconds
    
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("  MONITORING STOPPED")
        print("=" * 60)
        
        # Show final summary for each sensor
        print(f"\nFinal Summary ({reading_count} readings):")
        for sensor in sensors:
            avg = sensor.get_average_temp()
            print(f"  {sensor.location}: Avg {avg:.1f} C, "
                  f"{len(sensor.reading_history)} stored readings")
        
        stats = dashboard.get_mode_stats()
        print(f"\nDashboard: {stats['button_presses']} button presses")
        print(f"Mode usage: {stats['mode_counts']}")
        
        dashboard.set_led_state(False)
        print("\n[OK] Hardware cleaned up. Goodbye!")


if __name__ == "__main__":
    main()
