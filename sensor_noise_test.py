
def check_obstacle(distance):
    if distance < 15:
        return "STOP"
    elif distance < 30:
        return "SLOW"
    elif distance <= 50:
        return "CAUTION"
    else:
        return "MOVE FORWARD"


readings = [20, 21, 19, 22, 80]

average = sum(readings) / len(readings)
median = sorted(readings)[len(readings) // 2]

print("Readings:", readings)
print("Average:", average, "cm")
print("Median:", median, "cm")
print("Average-based action:", check_obstacle(average))
print("Median-based action:", check_obstacle(median))
