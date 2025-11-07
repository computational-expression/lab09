"""
Configuration Template for Lab 09

Copy this file to config.py and fill in your GitHub information.
DO NOT commit config.py to your repository (it's in .gitignore).

This file is used for automated grading and GitHub integration.
"""

# GitHub Configuration
GITHUB_USERNAME = "your-github-username"
STUDENT_NAME = "Your Full Name"
LAB_NUMBER = 9

# Hardware Configuration (for reference)
DHT22_PIN = 22
LDR_PIN = 26
LED_PIN = 15
BUTTON_PIN = 14

# Alert Thresholds (you can adjust these)
HIGH_TEMP_THRESHOLD = 28  # Celsius
LOW_TEMP_THRESHOLD = 16   # Celsius
HIGH_HUMIDITY_THRESHOLD = 70  # Percent
LOW_LIGHT_THRESHOLD = 600  # 0-1000 scale (higher = darker)

# Display Configuration
READING_INTERVAL = 2  # Seconds between readings
HISTORY_SIZE = 10  # Number of readings to keep in history
STATS_DISPLAY_INTERVAL = 10  # Display stats every N readings
