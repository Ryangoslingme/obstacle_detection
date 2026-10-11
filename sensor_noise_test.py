
def check_obstacle(distance):
    if distance < 15:
        return "STOP"
    elif distance < 30:
        return "SLOW"
    elif distance <= 50:
        return "CAUTION"
    else:
        return "MOVE FORWARD"


def calculate_median(readings):
    sorted_readings = sorted(readings)
    middle = len(sorted_readings) // 2
    return sorted_readings[middle]


readings = [20, 21, 19, 22, 80]

average = sum(readings) / len(readings)
median = calculate_median(readings)

print("Readings:", readings)
print("Average:", average, "cm")
print("Median:", median, "cm")
print("Average-based action:", check_obstacle(average))
print("Median-based action:", check_obstacle(median))
