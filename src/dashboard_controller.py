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
        # TODO: Initialize button_press_count to 0 to track statistics
        # TODO: Initialize mode_history as empty list to track mode changes
    
    def set_led_state(self, is_on):
        # TODO: Turn LED on or off based on is_on parameter (boolean)
    
    def blink_led(self, times, delay):
        # TODO: Blink LED specified number of times with delay between blinks
        # TODO: Use a loop to repeat the blink cycle
        # TODO: Turn LED on, sleep by delay seconds, turn LED off, sleep by delay seconds
    
    def read_button(self):
        # TODO: Read and return the current button state (0 or 1)
    
    def cycle_display_mode(self):
        # TODO: Cycle to the next display mode in the modes list
        # TODO: Handle wrapping from last mode back to first mode
        # TODO: Increment button_press_count by 1
        # TODO: Append the new display_mode to mode_history list
        # TODO: Call blink_led once with 0.1 second delay to confirm mode change
    
    def sound_buzzer(self, duration):
        # TODO: Play buzzer alert sound at specified duration in milliseconds
        # TODO: Set PWM frequency to 1000 Hz and duty cycle to 512 (50%)
        # TODO: Use time.sleep() with duration converted to seconds (duration / 1000)
        # TODO: Turn off buzzer by setting duty cycle to 0
    
    def indicate_alert(self, alert_data):
        # TODO: Check whether alert_data dictionary has 'any_alerts' set to True
        # TODO: When alerts are active: blink LED 3 times with 0.1 second delay, then sound buzzer at 200ms
        # TODO: When no alerts: turn LED off using set_led_state
    
    def get_mode_stats(self):
        # TODO: Create and return a dictionary with mode usage statistics
        # TODO: Include 'current_mode' (current display_mode string)
        # TODO: Include 'button_presses' (total button_press_count)
        # TODO: Include 'mode_counts' (dictionary counting occurrences of each mode in mode_history)
    
    def reset_stats(self):
        # TODO: Reset button_press_count to 0
        # TODO: Clear mode_history list
    
    def get_current_mode(self):
        # TODO: Return the current display_mode string
    
    def get_mode_display_title(self):
        # TODO: Return formatted title string based on current display_mode
        # TODO: Return "=== SUMMARY MODE ===" when mode is "summary"
        # TODO: Return "=== ALERTS MODE ===" when mode is "alerts"
        # TODO: Return "=== HISTORY MODE ===" when mode is "history"
        # TODO: Return "=== UNKNOWN MODE ===" otherwise


if __name__ == "__main__":
    # Test your implementation
    controller = DashboardController(15, 16, 14)
    print(f"Current mode: {controller.get_current_mode()}")
    controller.cycle_display_mode()
    print(f"After cycling: {controller.get_current_mode()}")

