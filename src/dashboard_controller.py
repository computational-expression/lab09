from machine import Pin, PWM
import time


class DashboardController:
    
    def __init__(self, led_pin, button_pin, buzzer_pin):
        # TODO: Initialize controller with LED, button, and buzzer pins
        # TODO: Set up LED as output pin
        # TODO: Set up button as input pin with pull-up resistor
        # TODO: Set up buzzer with PWM on specified pin
        # TODO: Initialize display_mode to "summary" (options: summary, history, alerts)
        # TODO: Create modes list containing all three display modes
        # TODO: Initialize button_press_count to 0 for tracking statistics
        # TODO: Initialize mode_history as empty list for tracking mode changes
    
    def set_led_state(self, is_on):
        # Turn LED on or off based on is_on parameter (boolean)
    
    def blink_led(self, times, delay):
        # Blink LED specified number of times with delay between blinks
        # Use a for loop to repeat the blink cycle
        # Turn LED on, sleep for delay seconds, turn LED off, sleep for delay seconds
    
    def read_button(self):
        # Read and return the current button state (0 or 1)
    
    def cycle_display_mode(self):
        # Cycle to the next display mode in the modes list
        # Handle wrapping from last mode back to first mode
        # Increment button_press_count by 1
        # Append the new display_mode to mode_history list
        # Call blink_led once with 0.1 second delay to confirm mode change
    
    def sound_buzzer(self, duration):
        # Play buzzer alert sound at specified duration in milliseconds
        # Set PWM frequency to 1000 Hz and duty cycle to 512 (50%)
        # Use time.sleep() with duration converted to seconds (duration / 1000)
        # Turn off buzzer by setting duty cycle to 0
    
    def indicate_alert(self, alert_data):
        # Check if alert_data dictionary has 'any_alerts' set to True
        # If alerts are active: blink LED 3 times with 0.1 second delay, then sound buzzer for 200ms
        # If no alerts: turn LED off using set_led_state
    
    def get_mode_stats(self):
        # Create and return a dictionary with mode usage statistics
        # Include 'current_mode' (current display_mode string)
        # Include 'button_presses' (total button_press_count)
        # Include 'mode_counts' (dictionary counting occurrences of each mode in mode_history)
    
    def reset_stats(self):
        # Reset button_press_count to 0
        # Clear mode_history list
    
    def get_current_mode(self):
        # Return the current display_mode string
    
    def get_mode_display_title(self):
        # Return formatted title string based on current display_mode
        # Return "=== SUMMARY MODE ===" if mode is "summary"
        # Return "=== ALERTS MODE ===" if mode is "alerts"
        # Return "=== HISTORY MODE ===" if mode is "history"
        # Return "=== UNKNOWN MODE ===" for any other mode


if __name__ == "__main__":
    # Test your implementation
    controller = DashboardController(15, 16, 14)
    print(f"Current mode: {controller.get_current_mode()}")
    controller.cycle_display_mode()
    print(f"After cycling: {controller.get_current_mode()}")

