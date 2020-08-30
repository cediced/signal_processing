"""
test the different fucntionnality of the module signal
"""

import unittest
import numpy as np

from signal_processing import signal


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
                                           average=0,
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


class TestFft(unittest.TestCase):
    def setUp(self):
        pass

    def test_fft_with_sinus(self):
        wanted_frequency = 5
        sig = signal.Signal.generate_sinus(sampling_rate=500,
                                           average=0,
                                           phase=0,
                                           frequency=wanted_frequency,
                                           duration=2)
        actual_frequency = sig.frequency()
        self.assertEqual(wanted_frequency, actual_frequency)


