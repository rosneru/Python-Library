import argparse
import os

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

  # Define the prefix which is added before each line
  prefix = '  File "..\\'

  # Create a list of files found in all Release directories below the solution directoy
  file_list = []
  for directories, _, files in os.walk(solution_dir):
    for file_name in files:
      rel_dir = os.path.relpath(directories, solution_dir)
      if rel_dir.endswith('Release'):
        if(not file_name.endswith('.txt') and
           not file_name.endswith('.pdb') and 
           not file_name.endswith('.cache') and 
           not file_name.endswith('.resources')):
          rel_file = os.path.join(rel_dir, file_name)
          file_list.append( prefix + rel_file + '"')

  try:
    output_file = open(output_file_path, "w")
  except:
    print('Failed to open output file \'{0}\' for writing.'.format(output_file_path))
    return

  for item in file_list:
    output_file.write(item + '\n')

  print("{0} lines written sucessfully to new created file '{1}'."
    .format(len(file_list), output_file_path))

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
                      metavar='solution file', 
                      help='The path to the solution file.')

  parser.add_argument('output_file_path', 
                      nargs=1, 
                      type=str,
                      metavar='result file', 
                      help='The path to the file to write the picked results into.')

  args = parser.parse_args()
  pick_files(args.solution_file_path[0], args.output_file_path[0])
  