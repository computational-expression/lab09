"""
Test Script for Button and LED

Tests the button input and LED output functionality for the dashboard controller.

Hardware Required:
- LED on GPIO 15
- Button on GPIO 16 (with pull-up resistor)

Author: TODO: Your name
Date: TODO: Date
"""

from machine import Pin
import time

def test_led():
    """Test LED blinking patterns."""
    print("\n=== Testing LED ===")
    print("LED should blink 5 times...")
    
    led = Pin(15, Pin.OUT)
    
    for i in range(5):
        led.value(1)  # On
        time.sleep(0.3)
        led.value(0)  # Off
        time.sleep(0.3)
    
    print("[OK] LED test complete!")


def test_button():
    """Test button input detection."""
    print("\n=== Testing Button ===")
    print("Press the button 5 times (you have 10 seconds)...")
    
    button = Pin(16, Pin.IN, Pin.PULL_UP)
    led = Pin(15, Pin.OUT)
    
    press_count = 0
    button_was_pressed = False
    start_time = time.time()
    
    while press_count < 5 and (time.time() - start_time) < 10:
        button_pressed = button.value() == 0  # Button uses pull-up
        
        if button_pressed and not button_was_pressed:
            press_count += 1
            led.value(1)  # Turn on LED when button pressed
            print(f"  Press {press_count} detected!")
            button_was_pressed = True
        elif not button_pressed:
            led.value(0)  # Turn off LED when button released
            button_was_pressed = False
        
        time.sleep(0.05)
    
    led.value(0)  # Ensure LED is off
    
    if press_count == 5:
        print("[OK] Button test complete!")
    else:
        print(f"[!] Only detected {press_count}/5 presses in time limit")


def test_button_led_together():
    """Test button controlling LED directly."""
    print("\n=== Testing Button + LED Together ===")
    print("Hold button to turn on LED (10 second test)...")
    
    button = Pin(16, Pin.IN, Pin.PULL_UP)
    led = Pin(15, Pin.OUT)
    
    start_time = time.time()
    
    while (time.time() - start_time) < 10:
        # LED on when button pressed, off when released
        button_pressed = button.value() == 0
        led.value(1 if button_pressed else 0)
        time.sleep(0.05)
    
    led.value(0)
    print("[OK] Button + LED test complete!")


if __name__ == "__main__":
    print("=" * 50)
    print("  BUTTON AND LED TEST SUITE")
    print("=" * 50)
    
    try:
        test_led()
        time.sleep(1)
        
        test_button()
        time.sleep(1)
        
        test_button_led_together()
        
        print("\n" + "=" * 50)
        print("  ALL TESTS COMPLETE!")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n\n[!] Tests interrupted by user")
        led = Pin(15, Pin.OUT)
        led.value(0)
