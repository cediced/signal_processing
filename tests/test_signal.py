"""
test the different fucntionnality of the module signal
"""

import unittest
import numpy as np
from decimal import Decimal

from signal_processing import signal


def generate_sinus_manually(time_s):
    t = np.linspace(0,1,10, endpoint=True)
    return np.sinus(2*np.pi * t)


class TestGenerateSinus(unittest.TestCase):
    """
    test if Signal can generate signals
    """

    def setUp(self):
        """
        init the test
        :return:
        """

    def test_generate_sinus(self):
        expected_frequency = 1
        sig = signal.Signal.generate_sinus(sampling_rate=100,
                                           average=150,
                                           phase=0,
                                           frequency=expected_frequency,
                                           duration=1)

        self.assertIsInstance(sig, signal.Signal)


    def test_sampling_is_right(self):
        """
        test if the sampling is respected
        :return:
        """
        how_long = 10
        for expected_sampling_rate in range(1, 100, 1):
            sig = signal.Signal.generate_sinus(sampling_rate=expected_sampling_rate,
                                               average=0,
                                               phase=0,
                                               frequency=10,
                                               duration=10)

            self.assertEqual(sig.values.shape[0], expected_sampling_rate*how_long)


    def test_average(self):
        wanted_average = 10
        sig = signal.Signal.generate_sinus(sampling_rate=10,
                                           average=wanted_average,
                                           phase=0,
                                           frequency=10,
                                           duration=10)
        self.assertEqual(round(sig.values.mean()), wanted_average)

    
    def test_phase(self):
        wanted_phase = np.pi/2
        sig = signal.Signal.generate_sinus(sampling_rate=10,
                                           average=0,
                                           phase=wanted_phase,
                                           frequency=10,
                                           duration=10)

        spectrum = np.fft.fft(sig.values)
        magnitude = np.abs(spectrum)
        phase = np.angle(spectrum)