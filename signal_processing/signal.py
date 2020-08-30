"""
help calculating frequency of a signal
"""
import numpy as np
import traceback


class Signal:
    """
    an advanced signal library
    """

    def __init__(self, values, sampling_rate):
        """
        :param values: values of the signal
        """
        self.values = values
        self.sampling_rate = sampling_rate

    @classmethod
    def generate_sinus(cls,
                       sampling_rate=1,
                       average=0,
                       phase=0,
                       frequency=2,
                       duration=10):
        """
        :param sampling_rate: sampling rate
        :param average: average of the signal
        :param phase: phase in radians
        :param frequency: frequency in herz
        :param duration: time in s
        :return: Signal object
        """
        time = np.linspace(0,
                           duration,
                           int(sampling_rate*duration), endpoint=False)

        values = np.sin(2 * np.pi * frequency * time + phase) + average
        return Signal(values, sampling_rate)

    def frequency(self):
        """
        :return: main frequency of the signal
        """


