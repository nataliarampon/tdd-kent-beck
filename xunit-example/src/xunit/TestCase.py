from xunit.TestResult import TestResult

class TestCase(object):
  def __init__(self, name):
    self.name = name
  
  def setUp(self):
    pass

  def run(self):
    self.setUp()
    method = getattr(self, self.name)
    method()
    self.tearDown()
    return TestResult()
  
  def tearDown(self):
    pass