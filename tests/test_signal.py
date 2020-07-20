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
        expected_frequency = 10
        sig = signal.Signal.generate_sinus(sampling_rate=20,
                                           average=150,
                                           phase=0,
                                           frequency=expected_frequency)

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

