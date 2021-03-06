from collections import namedtuple


class Pyrmission(object):
    accessor = None # The accessing-user
    context = None # Object of interest being accessed

    def __init__(self, user, ooi, ruleset):
        assert isinstance(user, dict)
        assert isinstance(ooi, dict)

        # Turn dict-input into objects-like structures
        self.accessor = namedtuple('Accessor', user.keys())(*user.values())
        self.context = namedtuple('Context', ooi.keys())(*ooi.values())

        self.access_control_rules = ruleset


    def is_allowed(self):
        try:
            return eval(self.access_control_rules, {}, self.__dict__)

        except SyntaxError as e:
            return False
