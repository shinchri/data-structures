"""
Problem 2: File Recursion
"""

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list = []
    _find_files(suffix, path, list) 
    return list

def _find_files(suffix, path, list):
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            list.append(path)

    if os.path.isdir(path):
        path_list = os.listdir(path)
        for a_path in path_list:
            _find_files(suffix, path + "/" + a_path, list)

    return list

result_list = find_files('.c', "./testdir")

for item in result_list:
    print(item)