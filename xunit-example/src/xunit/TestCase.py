class TestCase(object):
  def __init__(self, name):
    self.name = name

  def run(self):
    method = getattr(self, self.name)
    return method()