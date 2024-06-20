from xunit.TestCase import TestCase
from xunit.WasRun import WasRun

class TestCaseTest(TestCase):
  def setUp(self):
    self.test = WasRun('testMethod')

  def testSetUp(self):
    self.test.run()
    assert(self.test.log == 'setUp testMethod tearDown ')
  
  def testResult(self):
    self.test = WasRun('testMethod')
    result = self.test.run()
    assert('1 run, 0 failed' == result.summary())

TestCaseTest('testSetUp').run()
TestCaseTest('testResult').run()