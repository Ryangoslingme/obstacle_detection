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
