import math


def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """
    Convert the given angle to a sexagesimal string of hours of Right Ascension (RA).

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees.
    decimals : int, optional
        The number of decimal places for the seconds. Defaults to 3.

    Returns
    -------
    hms_str : str
        The sexagesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`.
    
    Raises
    ------
    OSError
        If 'decimals' is not an integer.
    """
    # Ensure the number of decimals is an integer
    if not isinstance(decimals, int):
        raise OSError('decimals should be an integer!')

    # Handle negative angles by taking the absolute value and storing the sign
    sign = '-' if angle_in_degrees < 0 else ''
    angle_in_degrees = abs(angle_in_degrees)

    # A full circle (360 degrees) is equal to 24 hours of RA.
    # Convert the angle from degrees to hours.
    hours_num = angle_in_degrees * 24 / 360
    
    # Calculate the integer part of the hours
    hours = math.floor(hours_num)

    # Calculate the remaining minutes from the fractional part of the hours
    min_num = (hours_num - hours) * 60
    minutes = math.floor(min_num)

    # Calculate the remaining seconds from the fractional part of the minutes
    seconds = (min_num - minutes) * 60

    # Format the output string with the calculated values
    format_string = f'{sign}{{0:d}}:{{1:02d}}:{{2:0{decimals+3}.{decimals}f}}'
    return format_string.format(hours, minutes, seconds)


print(angle_to_sexigesimal(5))
print(angle_to_sexigesimal(15.5, decimals=2))
print(angle_to_sexigesimal(-45))