import unittest
from pyrmission import Pyrmission

class PrimeTestCase(unittest.TestCase):

    def test_basic_ruleset(self):
        """
        This permission ruleset allows only user with
        with ID of 12 to access object of interest.
        """
        user = {'id': 12}
        ooi = {'foo': 'bar'} # Object of interest

        ruleset = 'accessor.id == 12'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertTrue(pyrmission.is_allowed())

        ruleset = 'accessor.id == 14'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertFalse(pyrmission.is_allowed())

        ruleset = 'accessor.id == 12 or context.foo == "bar"'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertTrue(pyrmission.is_allowed())


    def test_or_combo(self):
        pass

    def test_and_combo(self):
        pass

    def test_ranges(self):
        pass

    def test_time_pattern(self):
        pass

if __name__ == "__main__":
    unittest.main()
