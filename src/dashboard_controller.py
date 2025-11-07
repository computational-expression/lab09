"""
Dashboard Controller Module

This module provides the DashboardController class for managing LED indicators
and button input to create an interactive environmental monitoring dashboard.

Author: TODO: Your name
Date: TODO: Date
"""

# TODO: Import necessary libraries
# from machine import Pin
# import time


class DashboardController:
    """
    Manages dashboard display modes and user interaction via LED and button.
    
    Provides multiple display modes for viewing environmental data, tracks
    user interactions, and uses LED to indicate system status and alerts.
    
    Attributes:
        led_pin (int): GPIO pin number for LED indicator
        button_pin (int): GPIO pin number for mode button
        display_mode (str): Current display mode
        alert_active (bool): Whether environmental alerts are active
        button_press_count (int): Total number of button presses
        mode_history (list): List of display modes that were viewed
    """
    
    def __init__(self, led_pin, button_pin):
        """
        Initialize the DashboardController.
        
        Args:
            led_pin (int): GPIO pin for LED indicator
            button_pin (int): GPIO pin for mode button (with pull-up resistor)
        
        Example:
            dashboard = DashboardController(15, 14)
        """
        # TODO: Store pin numbers
        # TODO: Set up LED pin as output
        # TODO: Set up button pin as input with pull-up
        # TODO: Initialize display_mode to "temperature"
        # TODO: Initialize alert_active to False
        # TODO: Initialize button_press_count to 0
        # TODO: Initialize mode_history as empty list
        pass
    
    def set_led_state(self, is_on):
        """
        Turn LED on or off.
        
        Args:
            is_on (bool): True to turn LED on, False to turn off
        
        Example:
            dashboard.set_led_state(True)   # LED on
            dashboard.set_led_state(False)  # LED off
        """
        # TODO: Set LED pin value based on is_on boolean
        # Hint: Use 1 for on, 0 for off
        pass
    
    def blink_led(self, times, delay):
        """
        Blink LED a specified number of times.
        
        Args:
            times (int): Number of times to blink
            delay (float): Delay in seconds between blinks
        
        Example:
            dashboard.blink_led(3, 0.2)  # Blink 3 times, 0.2s delay
        """
        # TODO: Use a loop to blink LED the specified number of times
        # TODO: Turn LED on, wait delay seconds, turn LED off, wait delay seconds
        pass
    
    def read_button(self):
        """
        Check if button is currently pressed.
        
        Returns:
            bool: True if button is pressed, False otherwise
        
        Note:
            Button uses pull-up resistor, so pressed = 0, not pressed = 1
        
        Example:
            if dashboard.read_button():
                print("Button pressed!")
        """
        # TODO: Read button pin value
        # TODO: Return True if button is pressed (value == 0), False otherwise
        pass
    
    def cycle_display_mode(self):
        """
        Cycle to the next display mode when button is pressed.
        
        Display modes cycle in this order:
        "temperature" → "light" → "alerts" → "history" → "temperature" ...
        
        Also increments button_press_count and adds mode to mode_history.
        
        Example:
            if dashboard.read_button():
                dashboard.cycle_display_mode()
                print(f"New mode: {dashboard.display_mode}")
        """
        # TODO: Define list of modes: ["temperature", "light", "alerts", "history"]
        # TODO: Find current mode index in the list
        # TODO: Calculate next mode index (wrap around to 0 after last mode)
        # TODO: Update display_mode to next mode
        # TODO: Increment button_press_count
        # TODO: Add new mode to mode_history list
        # TODO: Blink LED once to confirm mode change
        pass
    
    def indicate_alert(self, alert_data):
        """
        Use LED to indicate alert status based on alert data.
        
        Args:
            alert_data (dict): Dictionary with alert information
                             Must contain 'any_alerts' key (bool)
        
        Behavior:
            - If any alerts: Blink LED rapidly (3 times, 0.1s delay)
            - If no alerts: Turn LED off
            - Updates alert_active attribute
        
        Example:
            alerts = sensor.check_alerts()
            dashboard.indicate_alert(alerts)
        """
        # TODO: Check if alert_data['any_alerts'] is True
        # TODO: If True:
        #       - Set alert_active to True
        #       - Blink LED 3 times with 0.1 second delay
        # TODO: If False:
        #       - Set alert_active to False
        #       - Turn LED off
        pass
    
    def get_mode_stats(self):
        """
        Get statistics about display mode usage and button presses.
        
        Returns:
            dict: Dictionary containing:
                - 'current_mode' (str): Current display mode
                - 'button_presses' (int): Total button presses
                - 'modes_viewed' (int): Number of different modes viewed
                - 'mode_counts' (dict): Count of how many times each mode viewed
        
        Example:
            stats = dashboard.get_mode_stats()
            print(f"Button pressed {stats['button_presses']} times")
        """
        # TODO: Create dictionary with current_mode and button_presses
        # TODO: Count how many modes have been viewed (length of mode_history)
        # TODO: Count occurrences of each mode in mode_history
        #       Hint: Loop through mode_history and count each mode
        # TODO: Add mode_counts dictionary to return dictionary
        # TODO: Return the complete stats dictionary
        pass
    
    def reset_stats(self):
        """
        Reset all usage statistics to initial values.
        
        Resets button_press_count to 0 and clears mode_history.
        Does not change current display_mode.
        
        Example:
            dashboard.reset_stats()
            print("Statistics reset!")
        """
        # TODO: Set button_press_count to 0
        # TODO: Clear mode_history (set to empty list)
        pass
    
    def get_mode_display_title(self):
        """
        Get display title for current mode.
        
        Returns:
            str: Formatted title string for current display mode
        
        Example:
            title = dashboard.get_mode_display_title()
            print(title)  # Might print: "=== TEMPERATURE MODE ==="
        """
        # TODO: Use if-elif-else to determine title based on display_mode
        # TODO: Return formatted title string with mode name in uppercase
        pass


# Test code - only runs when this file is executed directly
if __name__ == "__main__":
    print("Testing DashboardController class...")
    
    # TODO: Create a DashboardController object
    # TODO: Test LED on/off
    # TODO: Test LED blinking
    # TODO: Test button reading
    # TODO: Test mode cycling
    # TODO: Test getting statistics
    
    print("\nDashboardController test complete!")
