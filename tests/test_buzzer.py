"""
Test Script for Buzzer

Tests the buzzer alert functionality for the dashboard controller.

Hardware Required:
- Passive Buzzer on GPIO 14

Author: TODO: Your name
Date: TODO: Date
"""

from machine import Pin, PWM
import time

def test_buzzer_basic():
    """Test basic buzzer functionality."""
    print("\n=== Testing Buzzer - Basic Tones ===")
    print("Buzzer should produce 3 short beeps...")
    
    buzzer = PWM(Pin(14))
    buzzer.freq(1000)  # 1kHz tone
    
    for i in range(3):
        print(f"  Beep {i+1}")
        buzzer.duty_u16(32768)  # 50% duty cycle = on
        time.sleep(0.2)
        buzzer.duty_u16(0)  # Off
        time.sleep(0.3)
    
    buzzer.deinit()
    print("[OK] Basic buzzer test complete!")


def test_buzzer_frequencies():
    """Test different buzzer frequencies."""
    print("\n=== Testing Buzzer - Different Frequencies ===")
    print("Buzzer should produce tones at different pitches...")
    
    buzzer = PWM(Pin(14))
    frequencies = [500, 1000, 1500, 2000]
    
    for freq in frequencies:
        print(f"  Frequency: {freq} Hz")
        buzzer.freq(freq)
        buzzer.duty_u16(32768)
        time.sleep(0.5)
        buzzer.duty_u16(0)
        time.sleep(0.2)
    
    buzzer.deinit()
    print("[OK] Frequency test complete!")


def test_buzzer_alert_pattern():
    """Test buzzer alert pattern (like alarm)."""
    print("\n=== Testing Buzzer - Alert Pattern ===")
    print("Buzzer should produce an alert pattern (3 cycles)...")
    
    buzzer = PWM(Pin(14))
    
    for cycle in range(3):
        print(f"  Alert cycle {cycle+1}")
        # Fast beeping pattern
        buzzer.freq(1500)
        for _ in range(5):
            buzzer.duty_u16(32768)
            time.sleep(0.1)
            buzzer.duty_u16(0)
            time.sleep(0.1)
        time.sleep(0.5)
    
    buzzer.deinit()
    print("[OK] Alert pattern test complete!")


def test_buzzer_duration():
    """Test buzzer with specific durations."""
    print("\n=== Testing Buzzer - Duration Control ===")
    print("Testing 100ms, 200ms, 500ms durations...")
    
    buzzer = PWM(Pin(14))
    buzzer.freq(1000)
    durations = [100, 200, 500]
    
    for duration in durations:
        print(f"  Duration: {duration}ms")
        buzzer.duty_u16(32768)
        time.sleep(duration / 1000)
        buzzer.duty_u16(0)
        time.sleep(0.5)
    
    buzzer.deinit()
    print("[OK] Duration test complete!")


if __name__ == "__main__":
    print("=" * 50)
    print("  BUZZER TEST SUITE")
    print("=" * 50)
    
    try:
        test_buzzer_basic()
        time.sleep(1)
        
        test_buzzer_frequencies()
        time.sleep(1)
        
        test_buzzer_alert_pattern()
        time.sleep(1)
        
        test_buzzer_duration()
        
        print("\n" + "=" * 50)
        print("  ALL TESTS COMPLETE!")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n\n[!] Tests interrupted by user")
        buzzer = PWM(Pin(14))
        buzzer.duty_u16(0)
        buzzer.deinit()
