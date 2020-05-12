import argparse
import os

def pick_files(scan_depth: int, 
               path_solution: str, 
               path_output : str):
  # """ 
  # Generates a file with name ``file_name`` and fills it with as many
  # lines as given by parameter ``number_of_lines``. The file will
  # contain lines with right aligned numbers:

  # Line   1 Line   2
  # ...
  # Line   9
  # ....
  # Line  10
  # ...
  # Line  99 Line 100
  # """
  if path_output.endswith('.sln'):
    print("Error: An output file name ending with .sln is not allowed.")
    return

  if os.path.exists(path_solution) == False:
    print("Error: Solution file not found.")
    return

  solution_dir = os.path.dirname(path_solution)

  # Create a list of files found in all Release directories below the solution directoy
  directory_list = []
  for directories, _, files in os.walk(solution_dir):
    for file_name in files:
      rel_dir = os.path.relpath(directories, solution_dir)
      if(rel_dir.endswith('Release')):
        rel_file = os.path.join(rel_dir, file_name)
        directory_list.append(rel_file)

  print(directory_list)

  try:
      output_file = open(file_name, "w")
  except:
      print('Failed to open output file \'{0}\' for writing.'.format(path_output))
      return

  for item in directory_list:
    output_file.write(item + os.linesep)

  print("{0} lines written sucessfully to new created file '{1}'."
    .format(directory_list.count, path_output))

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
  pick_files(args.depth[0], args.path_solution[0], args.path_output[0])
  