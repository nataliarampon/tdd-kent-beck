from xunit.TestCase import TestCase
from xunit.WasRun import WasRun

class TestCaseTest(TestCase):
  def testSetUp(self):
    test = WasRun('testMethod')
    test.run()
    assert(test.wasSetUp)

  def testRunning(self):
    test = WasRun('testMethod')
    assert(not test.wasRun)
    test.run()
    assert(test.wasRun)
  
TestCaseTest('testRunning').run()
TestCaseTest('testSetUp').run()