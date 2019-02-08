""" Collection of file tools to quickly create test files etc """

from glob import glob
from os.path import exists, join

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
  if exists(file_name):
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

def multi_insert_src_class_object(dir_path, file_extension, 
  insert_text, insert_index):

  """ This function renames all files with extension ``file_extension``
  which are recursively found in directory ``dir_path``. It will 
  insert the ``insert_text`` at position ``insert_index`` into the file
  name. It will stick to the camel case rule, so the first letter after
  the inserted text will be a capital.
  
  In a second step it is reads the file itself search-and-replacing 
  all occurences of the old file name with the new filename (without 
  ``file_extension``).

  In this way text can be inserted into a bunch of Java/C++/C# classes 
  when the rule 'one-class-per-file' is adhered.

  NOTE ``file_extension`` can be a tuple or list cover multiple 
  extensions.
  """
  print("\nYou requested all '", file_extension ,"' files found in directory\n ", 
    dir_path,"\nto get the text '", insert_text,"' inserted at position " , 
    insert_index,"..\n\n", sep="")
    
#  typed = input("Continue (y/n) ? ")
#  if typed != "y":
#    print("Cancel.")
#    return

  all_files = []

  if isinstance(file_extension, (list, tuple)):
    for extension in file_extension:
      all_files.extend(glob(join(dir_path, extension)))
  else:
    all_files = glob(join(dir_path, file_extension))

  print("Listing all files:\n", all_files)

if __name__ == "__main__":
  # multi_insert_src_class_object("d:\DEV\Kruess\kr_tools_KruessBench\KruessBench\Views-KR-RICO", ".cs",  "rico", 0)
  multi_insert_src_class_object('e:\\Temp\\Testfiles', '*.cs',  'kric', 0)