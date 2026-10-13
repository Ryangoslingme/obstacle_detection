# Obstacle Detection Using Python

## Project Overview

This project explores basic obstacle-detection decision logic for a robotics application. It uses distance readings to select an appropriate robot action.

## Objective

To understand how conditional statements and functions can convert sensor distance readings into movement decisions.

## Technologies

* Python
* Conditional statements
* Functions
* Lists and loops

## Decision Logic

| Distance                  | Action       |
| ------------------------- | ------------ |
| Below 15 cm               | STOP         |
| 15 cm to below 30 cm      | SLOW         |
| 30 cm to 50 cm, inclusive | CAUTION      |
| Above 50 cm               | MOVE FORWARD |

## Sample Test Readings

`[10, 20, 30, 45, 50, 60]`

## What I Learned

* Writing a function that returns a decision.
* Using conditional statements to classify distance readings.
* Processing multiple readings using a loop.
* Handling boundary values in decision logic.

## Current Status

Day 1 completed: basic obstacle-detection logic.

## Future Improvements

* Compare consecutive sensor readings.
* Test noisy sensor data.
* Integrate sensor readings with a robot controller.

**Note:** This version uses sample distance values, not live hardware sensor measurements.

### Day 3: Sensor Noise and Filtering

**Topics learned:**
- Calculated the average of multiple simulated distance readings.
- Used the average distance with obstacle-detection decision logic.
- Learned how an extreme sensor reading can distort the average.
- Compared the mean and median to understand sensor filtering.

**Example readings:** `[20, 21, 19, 22, 80]`

- Average distance: `32.4 cm`
- Median distance: `21 cm`
- Average-based action: `CAUTION`
- Median-based action: `SLOW`

**Key learning:** The average can be affected by unusually high or low readings, while the median can be more robust to extreme readings.

**Status:** Completed Python simulation exercises. Readings are simulated, not live hardware measurements.

### Day 5 — Python + Webots Sensor Reading

- Connected a Python controller to a Webots robot.
- Read proximity sensor `ps0` using `sensor.getValue()`.
- Used a `while` loop to read the sensor continuously.
- Used `if/else` to classify sensor readings.
- Observed readings around 60–75 during testing.
- Obstacle-detection threshold still needs calibration; reliable detection has not yet been confirmed.
