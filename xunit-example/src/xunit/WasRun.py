from .TestCase import TestCase

class WasRun(TestCase):
  def __init__(self, name):
    self.wasRun = False
    self.wasSetUp = False
    TestCase.__init__(self, name)
  
  def setUp(self):
    self.wasSetUp = True

  def testMethod(self):
    self.wasRun = True