"""
Test suite for DashboardController class.
Tests LED control, button reading, and display mode management.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))

# Import mock modules first
import machine
import time

# Now import the student's code
from src.dashboard_controller import DashboardController


def test_initialization():
    """Test that controller initializes correctly."""
    print("Testing DashboardController initialization...")
    
    controller = DashboardController(15, 16, 14)
    
    # Check that pins are created
    assert hasattr(controller, 'led'), "Controller should have led attribute"
    assert hasattr(controller, 'button'), "Controller should have button attribute"
    assert hasattr(controller, 'buzzer'), "Controller should have buzzer attribute"
    
    # Check that display mode is initialized
    assert hasattr(controller, 'display_mode'), "Controller should have display_mode"
    assert controller.display_mode in ['summary', 'history', 'alerts'], \
        "display_mode should be one of: summary, history, alerts"
    
    # Check that modes list exists
    assert hasattr(controller, 'modes'), "Controller should have modes list"
    assert isinstance(controller.modes, list), "modes should be a list"
    assert len(controller.modes) == 3, "modes list should have 3 items"
    
    print("✓ Initialization test passed!")


def test_toggle_led():
    """Test LED on/off control."""
    print("\nTesting toggle_led method...")
    
    controller = DashboardController(15, 16, 14)
    
    # Test turning LED on
    controller.toggle_led(True)
    assert controller.led._state == True, "LED should be on"
    
    # Test turning LED off
    controller.toggle_led(False)
    assert controller.led._state == False, "LED should be off"
    
    print("✓ toggle_led test passed!")


def test_read_button():
    """Test reading button state."""
    print("\nTesting read_button method...")
    
    controller = DashboardController(15, 16, 14)
    
    # Test reading button (should return 0 or 1)
    button_state = controller.read_button()
    assert button_state in [0, 1], "Button state should be 0 or 1"
    
    print("✓ read_button test passed!")


def test_next_display_mode():
    """Test cycling through display modes."""
    print("\nTesting next_display_mode method...")
    
    controller = DashboardController(15, 16, 14)
    
    # Record initial mode
    initial_mode = controller.display_mode
    
    # Cycle to next mode
    controller.next_display_mode()
    second_mode = controller.display_mode
    
    # Should have changed
    assert second_mode != initial_mode or len(controller.modes) == 1, \
        "Display mode should change (unless only 1 mode exists)"
    
    # Cycle through all modes and back to start
    controller.next_display_mode()
    controller.next_display_mode()
    
    # After 3 cycles, should be back to initial mode (if 3 modes)
    if len(controller.modes) == 3:
        assert controller.display_mode == initial_mode, \
            "Should cycle back to initial mode after 3 cycles"
    
    print("✓ next_display_mode test passed!")


def test_play_alert_sound():
    """Test buzzer control."""
    print("\nTesting play_alert_sound method...")
    
    controller = DashboardController(15, 16, 14)
    
    # Test playing sound (should not raise error)
    try:
        controller.play_alert_sound(100)  # 100ms
        print("✓ play_alert_sound test passed!")
    except Exception as e:
        raise AssertionError(f"play_alert_sound raised an error: {e}")


def test_get_current_mode():
    """Test getting current display mode."""
    print("\nTesting get_current_mode method...")
    
    controller = DashboardController(15, 16, 14)
    
    # Get current mode
    current_mode = controller.get_current_mode()
    
    # Should match display_mode attribute
    assert current_mode == controller.display_mode, \
        "get_current_mode should return display_mode"
    
    # Should be a valid mode
    assert current_mode in ['summary', 'history', 'alerts'], \
        "Mode should be summary, history, or alerts"
    
    print("✓ get_current_mode test passed!")


def run_all_tests():
    """Run all test functions."""
    print("=" * 60)
    print("Running DashboardController Tests")
    print("=" * 60)
    
    try:
        test_initialization()
        test_toggle_led()
        test_read_button()
        test_next_display_mode()
        test_play_alert_sound()
        test_get_current_mode()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
