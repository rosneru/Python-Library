""" Collection of file tools to quickly create test files etc """

import os.path

def write_many_lines_to_file(file_name, number_of_lines):
  """ This function generates a file with name ``file_name`` and fills 
  it with as many lines as given by parameter ``numberOfLines``. The 
  file will contain lines with right aligned numbers:
  Line   1
  Line   2
  ...
  Line   9
  ....
  Line  10
  ...
  Line  99
  Line 100
  """
  if os.path.exists(file_name):
    print("Error: File already exists. Please provide another file name.")
    return

  try:
    output_file = open(file_name, "w")
  except:
    print("Error: File can't be opened. Please check your write permissions.")
    return

  maxDigits = len(str(number_of_lines))
  lineStr = "Line "
  for number in range(number_of_lines):
    numberStr = "{0:>{1}}".format(str(number), maxDigits)
    output_file.write(lineStr + numberStr + '\n')
  
  print("{0} lines written sucessfully to new created file '{1}'.".format(number_of_lines, file_name))
  output_file.close()
