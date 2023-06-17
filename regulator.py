import datetime

class DifferentialRegulator:
    COEFFICIENT = 0.1

    def __init__(self, time0=0, temp0=0, time1=None, temp1=None):
        """
        :param time0: time of the begining
        :param temp0: temperature of the begining
        :param time1: time of the end
        :param temp1: temperature of the end
        """
        self.temp1 = temp1
        self.temp0 = temp0
        self.time1 = time1
        self.time0 = time0

    def derivative(self):
        """
        calculate derivative of the given process
        :return: derivative of the given process dT / dt
        """
        return (self.temp1 - self.temp0) / (self.time1 - self.time0)

    def raising_time(self):
        """
        calculate raising time
        :return: raising time
        """
        return self.temp1 / self.derivative()

    def regulate(self):
        """
        the raising time should be bigget tha the dt bu the ten times
        it defines by the COEFFICIENT from the deffintions
        :return: the 0 if everything is OK, 1 if refrigerator must be switched on
        """
        if self.raising_time() < self.COEFFICIENT * (self.time1 - self.time0):
            return 0
        else:
            return 1


if __name__ == "__main__":
    regulator = DifferentialRegulator()

    with open("input.txt", "r") as fo:
        lines = fo.readlines()[1:]
        for i, line in enumerate(lines):
            _, temperature1 = line.strip().split(";")
            regulator.time1, regulator.temp1 = i + 1, float(temperature1)
            print(regulator.regulate())

            regulator.time0, regulator.temp0 = regulator.time1, regulator.temp1
