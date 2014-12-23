from os import path, sep, walk

def directory_search(directory, file_extension):
    """Creates an empty list, and then walks through all the subdirectories in
       the specified *directory*. At each folder in *directory* a search is 
       performed for files with the *file_extension* and adds the file and its
       parent directory to the empty list. The list is then returned to the
       caller."""
    file_list = []
    for dirpath, dirnames, files in walk(directory):
        for name in files:
            if name.endswith(file_extension):
                file_list.append(sep.join((dirpath, name)))
    
    return file_list
