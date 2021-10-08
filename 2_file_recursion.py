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


### TEST CASES ###

# Case 1
result_list = find_files('.c', "./testdir")

for item in result_list:
    print(item)

# Expected results:
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/t1.c
# ./testdir/subdir5/a.c
# ./testdir/subdir1/a.c

# Case 2
result_list = find_files('.d', "./testdir")

for item in result_list:
    print(item)

# Expected results:
# Nothing is printed out since there are no file that ends with '.d'

# Case 3
result_list = find_files('.d', "./testdirs")

for item in result_list:
    print(item)

# Expected results:
# Nothing is printed out because there are no directory './testdirs'