import glob
import unittest

from bandits.tests.test_helpers import Stats

test_files = glob.glob('*Test.py')
module_strings = [test_file[0:len(test_file)-3] for test_file in test_files]
suites = [unittest.defaultTestLoader.loadTestsFromName(test_file) for test_file in module_strings]
print(suites)
test_suite = unittest.TestSuite(suites)
test_runner = unittest.TextTestRunner().run(test_suite)

Stats.combine("./plots/")
