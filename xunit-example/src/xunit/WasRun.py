from .TestCase import TestCase

class WasRun(TestCase):
  def __init__(self, name):
    self.wasSetUp = False
    TestCase.__init__(self, name)
  
  def setUp(self):
    self.wasRun = False
    self.wasSetUp = True

  def testMethod(self):
    self.wasRun = True