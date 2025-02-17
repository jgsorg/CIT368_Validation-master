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
    if len(input) < 10 or len(input) > 20: # works for international numbers too (i think)
       return False
    #format
    phone_regex = r"^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    if not re.match(phone_regex, input):
        return False
    #diigt check
    digits_only = re.sub(r"\D", "", input)
    if len(digits_only) < 10:
        return False
    return True
