class TestResult(object):
  def __init__(self):
    self.runCount = 0
    self.errorCount = 0

  def testStarted(self):
    self.runCount += 1
  
  def testFailed(self):
    self.errorCount += 1

  def summary(self):
    return f'{self.runCount} run, {self.errorCount} failed'