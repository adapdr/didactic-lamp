"""
File contains tests for the `main.py` application file
"""
from unittest import TestCase

from webtest_asgi import TestApp

from src.main import app

TestApp.__test__ = False


class TestMain(TestCase):
    """
    Testcase for the `main.py` application file
    """

    app: TestApp

    def setUp(self):
        """
        Sets up ASGI Test App and global variables
        """
        # ASGI Test App
        self.app = TestApp(app)

        # TestCase Global Variables
