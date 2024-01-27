import re

class getSome:

  # get two arguments, which are regular expression and content for extraction
  def __init__(self, regex, content):
    self.regex = regex
    self.content = content

  def get(self):
    pattern = self.regex
    
    # extract all pattern from content 
    names = re.findall(pattern, self.content)

    # eliminate overlapped elements
    names = list(dict.fromkeys(names))

    return names






