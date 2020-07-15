"""
help calculating frequency of a signal
"""
import numpy as np


class Signal:
    """
    an advanced signal frequency analyser
    """
    def __init__(self, values, sampling_rate):
        """
        :param values: values of the signal
        """
        self.values = values
        self.sampling_rate = sampling_rate

    @classmethod
    def generate(cls,
                 function="sin",
                 sampling_rate=10,
                 average=0,
                 phase=0,
                 frequency=2,
                 how_long=10):
        """

        :param function: periodic function
        :param fps: sampling rate
        :param average: average of the signal
        :param phase: phase in radians
        :param frequency: frequency
        :param how_long: time in s
        :return: Signal object
        """
        time = range(0, how_long, how_long*sampling_rate)
        values = np.sin(time)
        return Signal(values, sampling_rate)

    def frequency(self):
        """
        :return: main frequency of the signal
        """
