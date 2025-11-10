"""
Dashboard Controller Module
TODO: Complete this class to manage LED indicators, buzzer alerts, and button input.
"""
from machine import Pin, PWM
import time


class DashboardController:
    """Controls display modes and user interaction via LED, buzzer, and button."""
    
    def __init__(self, led_pin, button_pin, buzzer_pin):
        """
        TODO: Initialize with LED, button, and buzzer on specified pins.
        - Create self.led = Pin(led_pin, Pin.OUT)
        - Create self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
        - Create self.buzzer = PWM(Pin(buzzer_pin))
        - Set self.buzzer.duty_u16(0) to start with buzzer off
        - Set self.display_mode = "temperature"
        - Set self.button_press_count = 0
        - Initialize self.mode_history as empty list
        """
        pass  # TODO: Replace with your code
    
    def set_led_state(self, is_on):
        """
        TODO: Turn LED on (True) or off (False).
        - If is_on is True, call self.led.on()
        - Otherwise, call self.led.off()
        """
        pass  # TODO: Replace with your code
    
    def blink_led(self, times, delay):
        """
        TODO: Blink LED specified number of times with delay between.
        - Use a for loop to repeat 'times' number of times
        - Turn LED on, sleep for 'delay', turn LED off, sleep for 'delay'
        """
        pass  # TODO: Replace with your code
    
    def read_button(self):
        """
        TODO: Check if button is pressed (pull-up: pressed = 0).
        - Return True if self.button.value() == 0
        - Return False otherwise
        """
        pass  # TODO: Replace with your code
    
    def cycle_display_mode(self):
        """
        TODO: Cycle to next display mode and record statistics.
        - Create list modes = ["temperature", "alerts", "history"]
        - Find current_index using modes.index(self.display_mode)
        - Calculate next_index = (current_index + 1) % len(modes)
        - Set self.display_mode = modes[next_index]
        - Increment self.button_press_count by 1
        - Append self.display_mode to self.mode_history
        - Call self.blink_led(1, 0.1) to confirm mode change
        """
        pass  # TODO: Replace with your code
    
    def sound_buzzer(self, duration):
        """
        TODO: Sound buzzer for alert (duration in milliseconds).
        - Set frequency: self.buzzer.freq(1000) for 1kHz tone
        - Turn on: self.buzzer.duty_u16(32768) for 50% duty cycle
        - Sleep for duration/1000 seconds (convert ms to seconds)
        - Turn off: self.buzzer.duty_u16(0)
        """
        pass  # TODO: Replace with your code
    
    def indicate_alert(self, alert_data):
        """
        TODO: Blink LED and sound buzzer if alerts active, otherwise turn off.
        - If alert_data['any_alerts'] is True:
          - Call self.blink_led(3, 0.1)
          - Call self.sound_buzzer(200) for short beep
        - Else:
          - Call self.set_led_state(False)
        """
        pass  # TODO: Replace with your code
    
    def get_mode_stats(self):
        """
        TODO: Get statistics about mode usage and button presses.
        - Create empty dictionary mode_counts = {}
        - Loop through each mode in self.mode_history:
          - If mode is in mode_counts, increment its count by 1
          - Otherwise, set mode_counts[mode] = 1
        - Return dictionary with keys: 'current_mode', 'button_presses', 'mode_counts'
        """
        pass  # TODO: Replace with your code
    
    def reset_stats(self):
        """
        TODO: Reset all usage statistics.
        - Set self.button_press_count = 0
        - Set self.mode_history = []
        """
        pass  # TODO: Replace with your code
    
    def get_mode_display_title(self):
        """
        TODO: Get formatted title for current display mode.
        - If self.display_mode == "temperature", return "=== TEMPERATURE MODE ==="
        - If self.display_mode == "alerts", return "=== ALERTS MODE ==="
        - If self.display_mode == "history", return "=== HISTORY MODE ==="
        - Otherwise, return "=== UNKNOWN MODE ==="
        """
        pass  # TODO: Replace with your code


if __name__ == "__main__":
    # Test your implementation
    dashboard = DashboardController(15, 16, 14)  # LED=15, Button=16, Buzzer=14
    
    print("Testing LED...")
    dashboard.blink_led(3, 0.2)
    
    print("Testing buzzer...")
    dashboard.sound_buzzer(500)
    
    print("Testing button and mode cycling...")
    for i in range(5):
        if dashboard.read_button():
            dashboard.cycle_display_mode()
            print(f"Mode: {dashboard.display_mode}")
        time.sleep(0.5)
    
    stats = dashboard.get_mode_stats()
    print(f"Presses: {stats['button_presses']}, Modes: {stats['mode_counts']}")
