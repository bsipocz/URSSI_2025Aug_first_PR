#modified by Venkatesh
import math

def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    # Check if the 'decimals' parameter is an integer. Raise an error if not.
    if math.floor(decimals) != decimals:
        raise OSError('decimals should be an integer!')

    # Convert the angle in degrees to hours. Since 360 degrees is equivalent to 24 hours,
    # we divide by 180 to convert to a range from 0 to 24 hours.
    hours_num = angle_in_degrees * 24 / 180
    
    # Extract the hour value by taking the floor (integer part) of the hours.
    hours = math.floor(hours_num)

    # Calculate the remaining fractional part of the hours in minutes.
    # Multiply the remainder by 60 to convert to minutes.
    min_num = (hours_num - hours) * 60
    
    # Extract the minute value by taking the floor of the calculated minutes.
    minutes = math.floor(min_num)

    # Calculate the remaining fractional part of the minutes in seconds.
    # Multiply the remainder by 60 to convert to seconds.
    seconds = (min_num - minutes) * 60

    # Format the hours, minutes, and seconds as a string with the specified number of decimal places for seconds.
    format_string = '{}:{}:{:.' + str(decimals) + 'f}'
    
    # Return the formatted string with hours, minutes, and seconds
    return format_string.format(hours, minutes, seconds)
