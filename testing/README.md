# Lab 09 Testing Structure

This lab includes automated test suites to verify student implementations of the `EnvironmentSensor` and `DashboardController` classes.

## Testing Folder Structure

```
lab09-starter/
└── testing/
    ├── machine.py                      # Mock MicroPython machine module
    ├── dht.py                          # Mock DHT sensor module
    ├── time.py                         # Mock/adapted time module
    ├── test_environment_sensor.py      # Tests for EnvironmentSensor class
    └── test_dashboard_controller.py    # Tests for DashboardController class
```

## Mock Modules

Since the lab uses MicroPython modules (`machine`, `dht`) that aren't available in standard Python, we provide mock modules that simulate hardware behavior:

### `machine.py`
- **Pin class**: Simulates GPIO pins with IN/OUT modes and PULL_UP resistors
- **PWM class**: Simulates PWM control for the buzzer

### `dht.py`
- **DHT22 class**: Simulates the temperature/humidity sensor
- Includes methods to set test values and simulate sensor errors

### `time.py`
- Adapts standard Python `time` module
- Adds MicroPython-specific functions like `sleep_ms()` and `ticks_ms()`

## Test Suites

### `test_environment_sensor.py`

Tests the following `EnvironmentSensor` methods:

1. **test_initialization**: Verifies proper initialization of location, reading_history, and dht_sensor
2. **test_read_conditions**: Tests reading temperature, humidity, and timestamp into a dictionary
3. **test_add_to_history**: Verifies reading history management (adding readings, limiting to 10)
4. **test_get_average_temp**: Tests average temperature calculation from history
5. **test_check_alerts**: Verifies alert detection for high/low temperature and high humidity

### `test_dashboard_controller.py`

Tests the following `DashboardController` methods:

1. **test_initialization**: Verifies proper initialization of LED, button, buzzer, and display modes
2. **test_toggle_led**: Tests LED on/off control
3. **test_read_button**: Tests reading button state
4. **test_next_display_mode**: Tests cycling through display modes (summary → history → alerts)
5. **test_play_alert_sound**: Tests buzzer control
6. **test_get_current_mode**: Tests retrieving current display mode

## Running Tests

### Individual Test Files

Run individual test suites from the lab directory:

```bash
# Test EnvironmentSensor
python3 testing/test_environment_sensor.py

# Test DashboardController
python3 testing/test_dashboard_controller.py
```

### Through GatorGrade

Tests are automatically run as part of GatorGrade checks:

```bash
gatorgrade --config config/gatorgrade.yml
```

The following GatorGrade checks run the tests:
- "EnvironmentSensor tests pass"
- "DashboardController tests pass"

## Test Output

Each test suite provides detailed output:

```
============================================================
Running EnvironmentSensor Tests
============================================================
Testing EnvironmentSensor initialization...
✓ Initialization test passed!

Testing read_conditions method...
✓ read_conditions test passed!

Testing add_to_history method...
✓ add_to_history test passed!

Testing get_average_temp method...
✓ get_average_temp test passed!

Testing check_alerts method...
✓ check_alerts test passed!

============================================================
ALL TESTS PASSED! ✓
============================================================
```

## What Students Need to Implement

For tests to pass, students must implement:

### EnvironmentSensor
- `__init__(location, temp_pin)`: Initialize sensor with location and DHT22 sensor
- `read_conditions()`: Read sensor and return dictionary with location, temperature, humidity, timestamp
- `add_to_history(reading)`: Add reading to history, keep last 10
- `get_average_temp()`: Calculate average temperature from history
- `check_alerts()`: Return dictionary with alert flags for temperature and humidity thresholds

### DashboardController
- `__init__(led_pin, button_pin, buzzer_pin)`: Initialize hardware and display modes
- `toggle_led(is_on)`: Turn LED on/off
- `read_button()`: Read button state
- `next_display_mode()`: Cycle through display modes
- `play_alert_sound(duration_ms)`: Play buzzer for specified duration
- `get_current_mode()`: Return current display mode string

## Benefits

1. **Immediate Feedback**: Students can run tests locally to verify their implementation
2. **Clear Requirements**: Tests document expected behavior and method signatures
3. **Hardware Independence**: Tests run on any Python environment without Pico hardware
4. **Automated Grading**: GatorGrade automatically runs tests for consistent evaluation
5. **Learning Tool**: Students can read tests to understand requirements and edge cases
