"""
Unit and regression test for the msf_2022b package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import numpy as np

import msf_2022b

def test_calculate_distance():
		"""Test that the calculate_distance function caculates what we expect"""
		r1 = np.array([0, 0, 0])
		r2 = np.array([0, 1.0, 0])
		expected_output = 1.0
		obeserved_output = msf_2022b.calculate_distance(r1, r2)

		assert expected_output == obeserved_output 

def test_msf_2022b_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "msf_2022b" in sys.modules
