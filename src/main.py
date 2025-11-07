"""
Environmental Monitoring Dashboard - Main Program

This program integrates the EnvironmentSensor and DashboardController classes
to create an interactive environmental monitoring system with multiple display modes.

Hardware Setup:
- DHT22 Temperature/Humidity sensor on GPIO 22
- LDR Photoresistor on GPIO 26 (ADC0)
- LED indicator on GPIO 15
- Mode button on GPIO 14

Author: TODO: Your name
Date: TODO: Date
"""

# TODO: Import necessary modules
# import time
# from environment_sensor import EnvironmentSensor
# from dashboard_controller import DashboardController


def display_temperature_mode(conditions):
    """
    Display temperature and humidity information.
    
    Args:
        conditions (dict): Dictionary with temperature and humidity data
    """
    # TODO: Print temperature mode header
    # TODO: Print temperature value with 1 decimal place
    # TODO: Print humidity value with 1 decimal place
    # TODO: Print temperature status (Cold/Comfortable/Warm)
    pass


def display_light_mode(conditions):
    """
    Display light level information.
    
    Args:
        conditions (dict): Dictionary with light_level data
    """
    # TODO: Print light mode header
    # TODO: Print light level value
    # TODO: Determine brightness category (Bright < 200, Medium 200-500, Dark > 500)
    # TODO: Print brightness category
    pass


def display_alerts_mode(alerts):
    """
    Display active environmental alerts.
    
    Args:
        alerts (dict): Dictionary with alert flags
    """
    # TODO: Print alerts mode header
    # TODO: Check if any alerts are active
    # TODO: If yes, list each active alert with ⚠️ symbol
    # TODO: If no, print "✓ All conditions normal"
    pass


def display_history_mode(sensor, conditions):
    """
    Display historical data averages.
    
    Args:
        sensor (EnvironmentSensor): Sensor object with history
        conditions (dict): Current conditions dictionary
    """
    # TODO: Print history mode header
    # TODO: Get and print average temperature from history
    # TODO: Print number of readings in history
    # TODO: Print current temperature for comparison
    pass


def main():
    """
    Main program loop for Environmental Monitoring Dashboard.
    
    Continuously monitors environmental conditions and displays information
    based on user-selected mode.
    """
    print("=" * 50)
    print("  ENVIRONMENTAL MONITORING DASHBOARD")
    print("=" * 50)
    print("\nInitializing hardware...")
    
    # TODO: Create EnvironmentSensor object with location "LAB_A", pins 22 and 26
    # TODO: Create DashboardController object with LED pin 15, button pin 14
    
    print("✓ Hardware initialized!")
    print("\nPress button to cycle display modes:")
    print("  1. Temperature  2. Light  3. Alerts  4. History")
    print("\nStarting monitoring...")
    print("-" * 50)
    
    # Variables to track button state (prevent multiple presses)
    button_was_pressed = False
    reading_count = 0
    
    try:
        # TODO: Create infinite loop (while True)
        while True:
            # --- BUTTON HANDLING ---
            # TODO: Read current button state
            # TODO: If button is pressed AND was not pressed before:
            #       - Cycle display mode
            #       - Update button_was_pressed to True
            # TODO: If button is not pressed:
            #       - Update button_was_pressed to False
            
            # --- SENSOR READING ---
            # TODO: Read environmental conditions from sensor
            # TODO: Add reading to sensor history
            # TODO: Check for alerts
            # TODO: Use dashboard to indicate alert status with LED
            
            # --- INCREMENT COUNTER ---
            reading_count += 1
            
            # --- DISPLAY INFORMATION ---
            # TODO: Print separator line
            # TODO: Print reading number and location
            # TODO: Get and print display mode title from dashboard
            
            # TODO: Use if-elif-else to display based on dashboard.display_mode
            # TODO: If mode is "temperature": call display_temperature_mode()
            # TODO: Elif mode is "light": call display_light_mode()
            # TODO: Elif mode is "alerts": call display_alerts_mode()
            # TODO: Elif mode is "history": call display_history_mode()
            
            # --- SHOW STATISTICS (every 10 readings) ---
            # TODO: If reading_count is divisible by 10:
            #       - Get mode statistics from dashboard
            #       - Print button press count and mode counts
            
            # TODO: Wait 2 seconds before next reading
            
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n" + "=" * 50)
        print("  MONITORING STOPPED")
        print("=" * 50)
        
        # TODO: Get final statistics from dashboard
        # TODO: Print final summary with total readings and button presses
        # TODO: Print goodbye message
        
        # TODO: Turn off LED
        print("\n✓ Hardware cleaned up. Goodbye!")


# Program entry point
if __name__ == "__main__":
    main()
