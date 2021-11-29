class CoordException(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

class SectionException(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

class EmptyCommandException(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

class MalformedCommandException(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

class IllegalCommandException(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

