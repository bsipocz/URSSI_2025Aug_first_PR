import math
from typing import Union


def angle_to_sexagesimal(angle_in_degrees: Union[float, int], decimals: int = 3) -> str:
    """
    Convert the given angle to a sexagesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float or int
        A scalar angle, expressed in degrees.
    decimals : int, optional
        The number of decimal places to round the seconds to.

    Returns
    -------
    hms_str : str
        The sexagesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`.

    Raises
    ------
    ValueError
        If `decimals` is not an integer.
    """
    if not isinstance(decimals, int):
        raise ValueError("decimals should be an integer!")

    if angle_in_degrees < 0 or angle_in_degrees > 360:
        raise ValueError("angle_in_degrees must be between 0 and 360")

    hours_num = angle_in_degrees * 24 / 360
    hours = int(hours_num)

    min_num = (hours_num - hours) * 60
    minutes = int(min_num)

    seconds = (min_num - minutes) * 60

    return f"{hours}:{minutes}:{seconds:.{decimals}f}"
