"""
Dashboard Controller Module - STARTER

Your task: Complete the DashboardController class methods.
"""
from machine import Pin
import time


class DashboardController:
    """Controls display modes and user interaction via LED and button."""
    
    def __init__(self, led_pin, button_pin):
        """Initialize with LED and button on specified pins."""
        # TODO: Set up LED pin as output
        # TODO: Set up button pin as input with pull-up
        # TODO: Initialize display_mode to "temperature"
        # TODO: Initialize button_press_count to 0
        # TODO: Initialize mode_history as empty list
        pass
    
    # TODO: Add set_led_state(self, is_on) method
    # Turn LED on (True) or off (False)
    
    # TODO: Add blink_led(self, times, delay) method
    # Blink LED specified number of times with delay between
    
    # TODO: Add read_button(self) method
    # Check if button is pressed (pull-up: pressed = 0)
    # Return True if pressed, False otherwise
    
    # TODO: Add cycle_display_mode(self) method
    # Cycle to next display mode: temperature → light → alerts → history
    # Update button_press_count and mode_history
    # Blink LED once to confirm
    
    # TODO: Add indicate_alert(self, alert_data) method
    # Blink LED 3 times if alerts active, otherwise turn off
    
    # TODO: Add get_mode_stats(self) method
    # Return dictionary with current_mode, button_presses, and mode_counts
    
    # TODO: Add reset_stats(self) method
    # Reset button_press_count to 0 and clear mode_history
    
    # TODO: Add get_mode_display_title(self) method
    # Return formatted title for current display mode


if __name__ == "__main__":
    # Test dashboard controller
    dashboard = DashboardController(15, 14)
    
    print("Testing LED...")
    dashboard.blink_led(3, 0.2)
    
    print("Testing button and mode cycling...")
    for i in range(5):
        if dashboard.read_button():
            dashboard.cycle_display_mode()
            print(f"Mode: {dashboard.display_mode}")
        time.sleep(0.5)
    
    stats = dashboard.get_mode_stats()
    print(f"Presses: {stats['button_presses']}, Modes: {stats['mode_counts']}")
