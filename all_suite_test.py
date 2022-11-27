import unittest

from unittest.loader import makeSuite

from test_cases.add_player import TestAddPlayerPage
from test_cases.check_dashboard import TestDashboardPage
from test_cases.login_to_the_system import TestLoginPage
from test_cases.framework import Test


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestDashboardPage))
    test_suite.addTest(makeSuite(TestAddPlayerPage))
    test_suite.addTest(makeSuite(Test))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
