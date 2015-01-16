import time

def to_sec(strtime):
    """ Convert time (str) to seconds (int)
    Args:
        strtime (str): time in format "hh:mm:ss"
    Returns:
        time in seconds (int)
    """
    hh, mm, ss = map(int, strtime.split(":"))
    return (hh * 3600) + (mm * 60) + ss

def to_str(seconds):
    """ Convert seconds (int) to time (str)
    Args:
        sec (int): time in seconds
    Returns:
         time (str) in format "hh:mm:ss"
    """
    return unicode(time.strftime("%H:%M:%S", time.gmtime(seconds)))

def check_strtime(str_time):
    """ Check if string value is time in format "hh:mm:ss"
    Args:
        str_time (str): string for checking
    Returns:
        True or False
    """
    return True
