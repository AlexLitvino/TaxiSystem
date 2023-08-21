"""This module contains helper functions"""

import math


def hours_to_minutes(hours: float):
    """Converts hours to minutes and rounds to smallest integer equal or greater than calculated minutes"""
    return math.ceil(hours * 60)
