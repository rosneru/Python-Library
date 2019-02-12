""" Collection of file tools to quickly create test files etc """

from glob import glob
import os

def write_many_lines_to_file(file_name, number_of_lines):
    """ 
    Generates a file with name ``file_name`` and fills it with as many 
    lines as given by parameter ``number_of_lines``. The file will 
    contain lines with right aligned numbers:

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

def multi_insert_src_class_object(dir_path, file_extension, 
                                  insert_text, insert_index):
    """ 
    Renames all files in directory ``dir_path`` whith extension 
    ``file_extension`` by inserting the string ``insert_text`` at index
    ``insert_index``.
    
    Additionally the file contents itself are read and all occurences 
    of the old plain name (without path and extension) are replaced by 
    the new plain name.

    In this way a directory containing multiple Java/C++/C# files
    can be renamed at one step together with the class names inside
    the files itself.

    Name creation is done following the CamelCase rule so the first 
    letter after the inserted text will be a capital.

    NOTE ``file_extension`` can be a tuple or list cover multiple 
    extensions.
    """

    # Ask the user if he really want to do it
    print("\nYou requested all '", file_extension,
        "' files found in directory\n ", dir_path, 
        "\nto get the text '", insert_text,"' inserted at position " , 
        insert_index,"..\n\n", sep="")
        
    answer = input("Continue (y/n) ? ")
    if answer != "y":
        print("Cancel.")
        return

    #
    # Creating a list of all files by extension in dir_path
    #

    all_files = []
    if isinstance(file_extension, (list, tuple)):
        # More then one extension given
        for extension in file_extension:
            all_files.extend(glob(os.path.join(dir_path, extension)))
    else:
        # Only one extension given
        all_files = glob(os.path.join(dir_path, file_extension))

    #
    # Traversing each file in list and decide how to rename it
    #
    for old_file_name_full_path in all_files:
        # Get file name without path
        old_file_name = os.path.basename(old_file_name_full_path)

        # Now splitting the file name. The '1' argument means that only
        # one split should be done. Everything after the first found 
        # separator will be in the [1] field of the split result.
        # 
        # So when splitting 'Example.cs.designer' split_result[0] will 
        # contain 'Example' and split_result[1] will contain the 
        # complete extension '.cs.Designer'.
        split_result = old_file_name.split(os.extsep, 1)

        old_plain_name = split_result[0]
        extension = split_result[1]

        # Creating a new plain name with the inseerted text at position
        new_plain_name = create_name_for_insert(old_plain_name, insert_text, insert_index)
        
        # Also create the full path with the new name
        new_file_name_full_path = os.path.join(dir_path, new_plain_name)
        new_file_name_full_path += extension

        # Rename the file
        os.rename(old_file_name_full_path, new_file_name_full_path)

        # Open the renamed file and read its contents
        with open(new_file_name_full_path, 'r') as file:
            file_content = file.read()

        # Replace all occurences of object name (plain name) in file
        file_content = file_content.replace(old_plain_name, new_plain_name)

        # Write the content into the file replacing its old content
        with open(new_file_name_full_path, 'w') as file:
            file.write(file_content)


def create_name_for_insert(old_name: str, insert_text: str, insert_index: int) -> str:
    """ 
    This function returns a new file name which is created from the 
    existing file name ``old_name`` by inserting ``insert_text`` 
    at the pos ``insert_index``.

    Name creation is done following the CamelCase rule so the first 
    letter after the inserted text will be a capital.
    """

    if len(old_name) < insert_index:
        return old_name + insert_text

    # The left part; the new string will be inserted after this
    left_part = old_name[:insert_index]

    # The right part; will be added after the new inserted string
    right_part_tmp = old_name[insert_index:]

    # The first char of the remaining part; will be changed to upper case
    right_first_char = right_part_tmp[:1]
    right_first_char = right_first_char.upper()

    # The remaining chars of the right part
    right_remaining_chars = right_part_tmp[1:]

    new_name = left_part + insert_text + right_first_char + right_remaining_chars
    return new_name


if __name__ == "__main__":
    # multi_insert_src_class_object("d:\DEV\Kruess\kr_tools_KruessBench\KruessBench\Views-KR-RICO", ".cs",    "rico", 0)
    multi_insert_src_class_object('e:\\Temp\\Testfiles', ('*.cs', '*.resx'),    'kric', 0)
