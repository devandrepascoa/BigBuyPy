import os
import sys

allowed_modes = ['devtest', 'test']


def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    import xmlrunner
    tests = unittest.TestLoader().discover('tests')
    # run tests with unittest-xml-reporting and output to $CIRCLE_TEST_REPORTS on CircleCI or test-reports locally
    xmlrunner.XMLTestRunner(output=os.environ.get(
        'CIRCLE_TEST_REPORTS', 'test-reports')).run(tests)


def devtest():
    from dotenv import load_dotenv
    load_dotenv()
    import unittest
    tests = unittest.TestLoader().discover('tests')
    import xmlrunner
    tests = unittest.TestLoader().discover('tests')
    # run tests with unittest-xml-reporting and output to $CIRCLE_TEST_REPORTS on CircleCI or test-reports locally
    xmlrunner.XMLTestRunner(output=os.environ.get(
        'CIRCLE_TEST_REPORTS', 'test-reports')).run(tests)


if __name__ == '__main__':
    mode = 'devtest'
    assert 1 <= len(
        sys.argv) <= 2, "Must have 1 argument(test,devtest) or none at all"

    if len(sys.argv) == 2:
        assert sys.argv[1] in allowed_modes, "Argument is not test or devtest"
        mode = sys.argv[1]

    if mode == 'devtest':
        devtest()
    elif mode == 'test':
        test()
