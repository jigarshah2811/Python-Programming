def getAngle(hour, minute):
    # Validations
    if hour < 0 or hour > 12 or minute < 0 or minute > 60:
        print("Invalid input")
        return
    """
    hour_angle = (hour*30) + (minute/2)
    min_angle = (minute*6)
    """
    hour_angle = 0.5 * (hour*60 + minute)
    min_angle = 6 * minute
    # Calculate hour and min hand angle diff
    angle = abs(hour_angle - min_angle)

    # Get the max out of 2 angles in clockwise & counter-clockwise
    print(min(angle, 360 - angle))


getAngle(9, 60)
getAngle(3, 30)
getAngle(12, 30)
getAngle(12, 00)
getAngle(11, 59)

