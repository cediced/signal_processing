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
        sig = signal.Signal.generate_sinus(function="sin",
                                           sampling_rate=20,
                                           average=150,
                                           phase=0,
                                           frequency=expected_frequency)

        self.assertIsInstance(sig, signal.Signal)

    def test_sampling_is_right(self):
        """
        test if the sampling is respected
        :return:
        """
        self.assert True == False

    def test_average_is_right(self):
        self.assert True == False