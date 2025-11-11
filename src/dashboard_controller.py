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
    
    def set_led_state(self, is_on):
        # Turn LED on or off based on is_on parameter (boolean)
    
    def read_button(self):
        # Read and return the current button state (0 or 1)
    
    def cycle_display_mode(self):
        # Cycle to the next display mode in the modes list
        # Handle wrapping from last mode back to first mode
    
    def sound_buzzer(self, duration):
        # Play buzzer alert sound at specified duration in milliseconds
        # Set PWM frequency to 1000 Hz and duty cycle to 512 (50%)
        # Use time.sleep_ms() with the duration value
        # Turn off buzzer by setting duty cycle to 0
    
    def display_sensor_data(self, sensor):
        # Display sensor data based on current display_mode
        # If mode is "summary", print sensor.get_status_summary()
        # If mode is "history", print last 5 readings from sensor.reading_history
        # If mode is "alerts", check sensor.check_alerts() and display any active alerts
    
    def process_button_press(self):
        # Handle button press to cycle through display modes
        # Read button state (0 = pressed on pull-up configuration)
        # If pressed, set LED on, play 100ms beep, cycle to next mode, add 200ms delay
        # If not pressed, set LED off
    
    def run_dashboard(self, sensors, check_interval=0.5):
        # Main dashboard loop that checks button and displays sensor data
        # Loop continuously checking button and updating display
        # Call process_button_press() to handle button input
        # Display data from each sensor in the sensors list
        # Sleep check_interval seconds between iterations
    
    def get_current_mode(self):
        # Return the current display_mode string


if __name__ == "__main__":
    # Test your implementation
    controller = DashboardController(15, 16, 14)
    print(f"Current mode: {controller.get_current_mode()}")
    controller.cycle_display_mode()
    print(f"After cycling: {controller.get_current_mode()}")

