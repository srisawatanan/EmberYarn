# test_emberyarn.py
"""
Tests for EmberYarn module.
"""

import unittest
from emberyarn import EmberYarn

class TestEmberYarn(unittest.TestCase):
    """Test cases for EmberYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EmberYarn()
        self.assertIsInstance(instance, EmberYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EmberYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
