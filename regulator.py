import matplotlib.pyplot as plt


class DifferentialRegulator:
    COEFFICIENT = 10

    def __init__(self, temp_max, temp_min, time0=0, temp0=0, time1=None, temp1=None):
        """
        :param time0: time of the begining
        :param temp0: temperature of the begining
        :param time1: time of the end
        :param temp1: temperature of the end
        """
        self.temp_max = temp_max
        self.temp_min = temp_min
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
        return (self.temp_max - self.temp_min) / self.derivative()

    def regulate(self):
        """
        the raising time should be bigget tha the dt by the ten times
        it defines by the COEFFICIENT from the defintions
        :return: the 0 if everything is OK, 1 if refrigerator must be switched on
        """
        if self.raising_time() > self.COEFFICIENT * (self.time1 - self.time0):
            return 0
        else:
            return 1


def exp_test():
    T_max = 1100
    T_min = 900
    fi = open("tests/f5exp.txt", "r")
    fo = open("tests/f6exp.txt", "w+")

    regulator = DifferentialRegulator(T_max, T_min)

    lines = fi.readlines()
    l = lines[0].strip().split(";")
    regulator.time0, regulator.temp0 = float(l[0]), float(l[1])

    # create lists to store the data for plotting
    times, temps, regs = [regulator.time0], [regulator.temp0], [0]

    for line in lines[1:]:
        l = line.strip().split(";")
        regulator.time1, regulator.temp1 = float(l[0]), float(l[1])
        res = regulator.regulate()
        fo.write(str(res) + "\n")
        regulator.time0, regulator.temp0 = regulator.time1, regulator.temp1

        # append data to the lists for plotting
        times.append(regulator.time1)
        temps.append(regulator.temp1)
        regs.append(res)

    fi.close()
    fo.close()

    # plot the data
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (°C)', color=color)
    ax1.plot(times, temps, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Regulated Value', color=color)
    ax2.plot(times, regs, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    # add horizontal lines
    ax1.axhline(y=T_max, linestyle='--', color='k')
    ax1.axhline(y=T_min, linestyle='--', color='k')

    fig.tight_layout()
    plt.show()


def sin_test1():
    fi = open("tests/f5sin.txt", "r")
    fo = open("tests/f6sin.txt", "w+")

    T_max = 1100
    T_min = 900

    regulator = DifferentialRegulator(T_max, T_min)

    lines = fi.readlines()
    l = lines[0].strip().split(";")
    regulator.time0, regulator.temp0 = float(l[0]), float(l[1])

    # create lists to store the data for plotting
    times, temps, regs = [regulator.time0], [regulator.temp0], [0]

    for line in lines[1:]:
        l = line.strip().split(";")
        regulator.time1, regulator.temp1 = float(l[0]), float(l[1])
        res = regulator.regulate()
        fo.write(str(res) + "\n")
        regulator.time0, regulator.temp0 = regulator.time1, regulator.temp1

        # append data to the lists for plotting
        times.append(regulator.time1)
        temps.append(regulator.temp1)
        regs.append(res)

    fi.close
    fo.close

    # plot the data
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (°C)', color=color)
    ax1.plot(times, temps, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Regulated Value', color=color)
    ax2.plot(times, regs, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    # add horizontal lines
    ax1.axhline(y=T_max, linestyle='--', color='k')
    ax1.axhline(y=T_min, linestyle='--', color='k')

    fig.tight_layout()
    plt.show()

def sin_test2():
    fi = open("tests/f5sin.txt", "r")
    fo = open("tests/f6sin.txt", "w+")
    T_max = 1500
    T_min = 300
    regulator = DifferentialRegulator(T_max, T_min)

    lines = fi.readlines()
    l = lines[0].strip().split(";")
    regulator.time0, regulator.temp0 = float(l[0]), float(l[1])

    # create lists to store the data for plotting
    times, temps, regs = [regulator.time0], [regulator.temp0], [0]

    for line in lines[1:]:
        l = line.strip().split(";")
        regulator.time1, regulator.temp1 = float(l[0]), float(l[1])
        res = regulator.regulate()
        fo.write(str(res) + "\n")
        regulator.time0, regulator.temp0 = regulator.time1, regulator.temp1

        # append data to the lists for plotting
        times.append(regulator.time1)
        temps.append(regulator.temp1)
        regs.append(res)

    fi.close
    fo.close

    # plot the data
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (°C)', color=color)
    ax1.plot(times, temps, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Regulated Value', color=color)
    ax2.plot(times, regs, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    # add horizontal lines
    ax1.axhline(y=T_max, linestyle='--', color='k')
    ax1.axhline(y=T_min, linestyle='--', color='k')

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    # regulator = DifferentialRegulator(100, 90)
    #
    # fr = open("f5.txt", "r")
    # fw = open("f6.txt", "w+")
    # lines = fr.readlines()[1:]
    # for i, line in enumerate(lines):
    #     _, temperature1 = line.strip().split(";")
    #     regulator.time1, regulator.temp1 = i + 1, float(temperature1)
    #     res = regulator.regulate()
    #     if res:
    #         fw.write(str(regulator.time1)+"\n")
    #
    #     regulator.time0, regulator.temp0 = regulator.time1, regulator.temp1
    # exp_test()
    # sin_test1()
    sin_test2()
