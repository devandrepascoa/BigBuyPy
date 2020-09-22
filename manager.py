import os
if __name__ == '__main__':
    import unittest
    tests = unittest.TestLoader().discover('tests')
    import xmlrunner
    tests = unittest.TestLoader().discover('tests')
    # run tests with unittest-xml-reporting and output to $CIRCLE_TEST_REPORTS on CircleCI or test-reports locally
    xmlrunner.XMLTestRunner(output=os.environ.get(
        'CIRCLE_TEST_REPORTS', 'test-reports')).run(tests)