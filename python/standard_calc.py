def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    new_angle = float(angle) % 360
    if new_angle >= 180:
        new_angle -= 360
    return new_angle


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    if second_angle > first_angle:
        bigger_angle = second_angle
        smaller_angle = first_angle
    else:
        bigger_angle = first_angle
        smaller_angle = second_angle

    clockwise_angle = bigger_angle - smaller_angle
    counter_clockwise_angle = 360 - clockwise_angle

    if middle_angle > smaller_angle and middle_angle < bigger_angle:
        if clockwise_angle < counter_clockwise_angle:
            return True
        else:
            return False
    elif clockwise_angle > counter_clockwise_angle:
        return True
    else:
        return False
