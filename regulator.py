from defifintions import COEFFICIENT
"""
    :param temp1: temperature of the end
    :param temp0: temperature of the begining
    :param time1: time of the end
    :param time0: time of the begining
"""
def derivative(temp1, temp0, time1, time0):
    """
    calculate derivative of the given process
    :return: derivative of the given process dT / dt
    """
    return (temp1 - temp0) / (time1 - time0)

def raising_time(temp1, temp0, time1, time0):
    """
    calculate raising time
    :return: raising time
    """
    return temp1 / derivative(temp1, temp0, time1, time0)

def regulate(temp1, temp0, time1, time0):
    """
    the raising time should be bigget tha the dt bu the ten times
    it defines by the COEFFICIENT from the deffintions
    :return: the 0 if everything is OK, 1 if refrigerator must be switched on
    """
    if raising_time(temp1, temp0, time1, time0) < COEFFICIENT * (time1 - time0):
        return 0
    else:
        return 1


def get_data():

if __name__ == "__main__":

 while True:
