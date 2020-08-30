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
                           num=int(sampling_rate*duration),
                           endpoint=True)

        values = np.sin(2 * np.pi * frequency * time + phase) + average
        return Signal(values, sampling_rate)

    def frequency(self):
        """
        :return: main frequency of the signal
        """
        fourrier_transform = np.fft.fft(self.values) / len(self.values)  # normalized fourrier trasform
        fourrier_transform = fourrier_transform[range(int(len(self.values)/2))]  # get rid of negative frequency

        tpCount = len(self.values)
        values = np.arange(int(tpCount / 2))
        timePeriod = tpCount / self.sampling_rate

        frequencies = values / timePeriod
        max_peak = np.argmax(np.abs(fourrier_transform))
        result = frequencies[max_peak]
        return result
