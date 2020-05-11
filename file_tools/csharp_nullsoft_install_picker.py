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
  parser = argparse.ArgumentParser(description='Scans the projects '
                                   'relative to a C# solution file and '
                                   'picks all .dll / .config / .exec '
                                   'files of each project, then adds '
                                   'them to the output file. Can be '
                                   'helpful when manually creating '
                                   'install scripts for Nullsoft '
                                   'installer.')

  parser.add_argument('depth', metavar='depth', nargs=1, type=int,
                      help='The depth of directory hierarchie to scan')

  parser.add_argument('path_solution', metavar='solution file', nargs=1, type=str,
                      help='The path to the solution file.')

  parser.add_argument('path_output', metavar='result file', nargs=1, type=str,
                      help='The path to the file to write the picked results into.')

  args = parser.parse_args()
  write_many_lines_to_file(args.file_name, args.n)
  