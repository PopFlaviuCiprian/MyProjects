import unittest
import HtmlTestRunner
from testing_site_Emag import Emag
from tests_press_alerts import Alerts
from test_login import Login
from test_google import Google
from test_google_search import Google_search

class TestSuite(unittest.TestCase):
    def test_suite(self):

        test_to_run = unittest.TestSuite()

        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Emag),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Google),
            unittest.defaultTestLoader.loadTestsFromTestCase(Google_search)
            # here we can add more tests
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title = 'Testing reports',
            report_name= "Suite test report"
        )
        runner.run(test_to_run)