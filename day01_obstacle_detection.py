
def check_obstacle(distance):
    if distance < 15:
        return "STOP"
    elif distance < 30:
        return "SLOW"
    elif distance <= 50:
        return "CAUTION"
    else:
        return "MOVE FORWARD"

readings = [10, 20, 30, 45, 50, 60]

for distance in readings:
    action = check_obstacle(distance)
    print(distance, "cm ->", action)