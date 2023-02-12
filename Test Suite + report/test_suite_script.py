import unittest
import HtmlTestRunner
from testing_site_Emag import Emag

class TestSuite(unittest.TestCase):
    def test_suite(self):

        test_to_run = unittest.TestSuite()

        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Emag)
            # here we can add more tests
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title = 'Testing reports',
            report_name= "Suite test report"
        )
        runner.run(test_to_run)