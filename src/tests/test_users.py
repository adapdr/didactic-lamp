"""
File contains tests for 'users' features
"""
from unittest import TestCase

from webtest_asgi import TestApp

from src.main import app

TestApp.__test__ = False


class TestUsers(TestCase):
    """
    Testcases for 'users' features
    """

    app: TestApp

    def setUp(self):
        """
        Sets up ASGI Test App and global variables
        """
        # ASGI Test App
        self.app = TestApp(app)

        # TestCase Global Variables

    # TODO: Implement test cases
