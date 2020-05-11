import argparse
import os

def write_many_lines_to_file(file_name: str, number_of_lines: int):
  """ 
  Generates a file with name ``file_name`` and fills it with as many
  lines as given by parameter ``number_of_lines``. The file will
  contain lines with right aligned numbers:

  Line   1 Line   2
  ...
  Line   9
  ....
  Line  10
  ...
  Line  99 Line 100
  """

  if os.path.exists(file_name):
      print("Error: File already exists.")
      return

  try:
      output_file = open(file_name, "w")
  except:
      print("Error: File can't be opened for writing.")
      return

  maxDigits = len(str(number_of_lines))
  lineStr = "Line "
  for number in range(number_of_lines):
      numberStr = "{0:>{1}}".format(str(number), maxDigits)
      output_file.write(lineStr + numberStr + '\n')
  
  print("{0} lines written sucessfully to new created file '{1}'."
    .format(number_of_lines, file_name))

  output_file.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Creates a text file '
                                   'with the given number of lines.')

  parser.add_argument('number_of_lines', metavar='n', nargs=1, type=int,
                      help='The number of lines to be written into file.')

  parser.add_argument('file_name', metavar='file', nargs=1, type=str,
                      help='The name of the file to be created.')

  args = parser.parse_args()
  write_many_lines_to_file(args.file_name, args.n)
  