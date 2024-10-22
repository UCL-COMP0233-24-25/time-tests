import pytest
from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", number_of_intervals=1, gap_between_intervals_s=0)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", number_of_intervals=2, gap_between_intervals_s=60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    # judge that the result matches the expected value
    assert result == expected, f"Expected: {expected}, but Result: {result}, doesn't match!"