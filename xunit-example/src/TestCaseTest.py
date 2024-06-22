from xunit.TestCase import TestCase
from xunit.WasRun import WasRun
from xunit.TestResult import TestResult
from xunit.TestSuite import TestSuite

class TestCaseTest(TestCase):
  def setUp(self):
    self.result = TestResult()

  def testOrder(self):
    test = WasRun('testMethod')
    test.run(self.result)
    assert(test.log == 'setUp testMethod tearDown ')
  
  def testResult(self):
    test = WasRun('testMethod')
    test.run(self.result)
    assert('1 run, 0 failed' == self.result.summary())

  def testFailedResult(self):
    test = WasRun('testBrokenMethod')
    test.run(self.result)
    assert('1 run, 1 failed' == self.result.summary())
  
  def testFailedResultFormatting(self):
    result = TestResult()
    result.testStarted()
    result.testFailed()
    assert('1 run, 1 failed' == result.summary())
  
  def testSuite(self):
    suite = TestSuite()
    suite.add(WasRun('testMethod'))
    suite.add(WasRun('testBrokenMethod'))
    suite.run(self.result)
    assert('2 run, 1 failed' == self.result.summary())

suite = TestSuite()
suite.add(TestCaseTest('testOrder'))
suite.add(TestCaseTest('testResult'))
suite.add(TestCaseTest('testFailedResult'))
suite.add(TestCaseTest('testFailedResultFormatting'))
suite.add(TestCaseTest('testSuite'))
result = TestResult()
suite.run(result)
print(result.summary())