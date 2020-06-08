import argparse
import os
from pathlib import Path

# Scans the projects relative to a C# solution file and picks all .dll /
# .config / .exec files of each project, then adds them to the output
# file. Can be helpful when manually creating install scripts for
# Nullsoft installer.

def pick_files(solution_file_path: str, 
               output_file_path : str):
  if output_file_path.endswith('.sln'):
    print("Error: An output file name ending with .sln is not allowed.")
    return

  if os.path.exists(solution_file_path) == False:
    print("Error: Solution file not found.")
    return

  solution_dir = os.path.dirname(solution_file_path)

  # Create a list of files found in all Release directories below the solution directoy
  result_script = []
  for directories, dirnames, _ in os.walk(solution_dir):
    if 'obj' in dirnames:
      dirnames.remove('obj')

    if directories.endswith('Release'):
      # construct the destination dir and create the nullsoft installer command
      path = Path(directories)
      a = path.parent.parent.parent.name
      b = path.parent.parent.name
      nullsoft_path_cmd = '  SetOutPath "$INSTDIR\{0}.{1}"'.format(a, b)
      result_script.append(nullsoft_path_cmd)

      # add all .dll files from source dir
      rel_dir = os.path.relpath(directories, solution_dir)
      rel_file = os.path.join(rel_dir, "*.dll")
      nullsoft_file_cmd = '  File "..\\{0}"'.format(rel_file)
      result_script.append(nullsoft_file_cmd)   

      # add all .exe files from source dir
      rel_file = os.path.join(rel_dir, "*.exe")
      nullsoft_file_cmd = '  File "..\\{0}"'.format(rel_file)
      result_script.append(nullsoft_file_cmd)  

      # add all .config files from source dir
      rel_file = os.path.join(rel_dir, "*.config")
      nullsoft_file_cmd = '  File "..\\{0}"'.format(rel_file)
      result_script.append(nullsoft_file_cmd)   

      # add all .xml files from source dir
      rel_file = os.path.join(rel_dir, "*.xml")
      nullsoft_file_cmd = '  File "..\\{0}"'.format(rel_file)
      result_script.append(nullsoft_file_cmd)  

      # add an empty line as separator
      result_script.append('')

  try:
    output_file = open(output_file_path, "w")
  except:
    print('Failed to open output file \'{0}\' for writing.'.format(output_file_path))
    return

  for item in result_script:
    output_file.write(item + '\n')

  print("{0} lines written sucessfully to new created file '{1}'."
    .format(len(result_script), output_file_path))

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

  parser.add_argument('solution_file_path', 
                      nargs=1, 
                      type=str,
                      metavar='solution_file', 
                      help='The path to the solution file.')

  parser.add_argument('output_file_path', 
                      nargs=1, 
                      type=str,
                      metavar='result_file', 
                      help='The path to the file to write the picked results into.')

  args = parser.parse_args()
  pick_files(args.solution_file_path[0], args.output_file_path[0])
  