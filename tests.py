import unittest
from pyrmission import Pyrmission

class PrimeTestCase(unittest.TestCase):

    def test_basic_ruleset(self):
        """
        This permission ruleset allows only user with
        with ID of 12 to access object of interest.
        """
        user = {'id': 12}
        ooi = {}

        ruleset = 'accessor.id == 12'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertTrue(pyrmission.is_allowed())

        ruleset = 'accessor.id == 14'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertFalse(pyrmission.is_allowed())


    def test_or_combo(self):
        user = {'id': 18}
        ooi = {'foo': 'bar'} # Object of interest

        ruleset = 'accessor.id == 12 or context.foo == "bar"'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertTrue(pyrmission.is_allowed())

        ruleset = 'accessor.id == 12 or context.foo == "mattis"'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertFalse(pyrmission.is_allowed())

        ruleset = 'accessor.id == 18 or context.foo == "mattis"'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertTrue(pyrmission.is_allowed())


    def test_and_combo(self):
        user = {'id': 18}
        ooi = {'foo': 'bar'} # Object of interest

        ruleset = 'accessor.id == 18 and context.foo == "bar"'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertTrue(pyrmission.is_allowed())

        ruleset = 'accessor.id == 12 and context.foo == "bar"'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertFalse(pyrmission.is_allowed())

        ruleset = 'accessor.id == 18 and context.foo == "erat"'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertFalse(pyrmission.is_allowed())


    def test_ranges(self):
        user = {'posuere': 20.7}
        ooi = {}

        ruleset = '18.5 < accessor.posuere < 22.8'
        pyrmission = Pyrmission(user, ooi, ruleset)
        self.assertTrue(pyrmission.is_allowed())


    def test_bad_ruleset(self):
        # Gibberish ruleset
        ruleset = 'Aliquam posuere Nam euismod tellus id erat'
        pyrmission = Pyrmission({}, {}, ruleset)
        self.assertFalse(pyrmission.is_allowed())


if __name__ == "__main__":
    unittest.main()
