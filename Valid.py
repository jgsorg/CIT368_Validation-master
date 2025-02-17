import re

class Valid:
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def zip(input):
    #length?
    if len(input) != 5:
        return False
    #digits?
    if not input.isdigit():
        return False
    #real ZIP?
    if not re.match(r"^\d{5}$", input):
        return False
    return True
  
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def phone(input):
    #length?

    #digits?

    #format?

    #real number?
    
    return True

    #testing commits