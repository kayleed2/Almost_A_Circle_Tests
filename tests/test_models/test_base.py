#!/usr/bin/python3
"""Unittesting for the Base module/class
Tests are done for each method of the class"""


import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassBase(unittest.TestCase):
    """Test class for testing Base class"""

    def test_pep8_base(self):
            """
            Test that models/base.py is pep8 compliant.
            """
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/base.py'])
            self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")
