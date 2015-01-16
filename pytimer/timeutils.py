import time

def to_sec(strtime):
    """ Convert time in str to int seconds
    Args:
        strtime (str): time in format "hh:mm:ss"
    """
    hh, mm, ss = map(int, strtime.split(":"))
    return (hh * 3600) + (mm * 60) + ss

def to_str(seconds):
    """ Convert seconds to time in format "hh:mm:ss"
    Args:
        sec (int): time in seconds
    """
    return unicode(time.strftime("%H:%M:%S", time.gmtime(seconds)))

def check_strtime(str_time):
    """ Check if string value is time in format "hh:mm:ss"
    Args:
        str_time (str): 
    """
    return True
