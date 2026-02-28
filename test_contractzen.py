# test_contractzen.py
"""
Tests for ContractZen module.
"""

import unittest
from contractzen import ContractZen

class TestContractZen(unittest.TestCase):
    """Test cases for ContractZen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ContractZen()
        self.assertIsInstance(instance, ContractZen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ContractZen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
