
def check_obstacle(distance):
    if distance < 15:
        return "STOP"
    elif distance < 30:
        return "SLOW"
    elif distance <= 50:
        return "CAUTION"
    else:
        return "MOVE FORWARD"


def calc_median(readings):
    sorted_readings = sorted(readings)
    middle = len(sorted_readings) // 2

    if len(sorted_readings) % 2 == 1:
        return sorted_readings[middle]
    else:
        return (sorted_readings[middle - 1] +
                sorted_readings[middle]) / 2


readings = [10, 20, 30, 40]

filtered_distance = calc_median(readings)
action = check_obstacle(filtered_distance)

print("Readings:", readings)
print("Filtered distance:", filtered_distance, "cm")
print("Robot action:", action)
