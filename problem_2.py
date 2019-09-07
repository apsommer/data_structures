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

    # initialize a blank list to hold all files with passed suffix
    files = []

    # recursive layer
    def _find_files(suffix, path, files):

        # all files and directories on this level
        items = os.listdir(path)

        # loop through all files and directories on this level
        while len(items) > 0:

            # pop this item off the list and analyze its structure
            item = items.pop()

            # full path name for this layer
            sub_path = path + '/' + item

            # directory name, does not include the . separator
            if '.' not in item:

                # recurisve call into next subdirectory
                files = _find_files(suffix, sub_path, files)

            # file name, check if it has the passed suffix
            if item.endswith(suffix):

                # append the full path and filename to the output list
                files.append(sub_path)

        # return the list up a recursive layer
        return files

    # start recursion with the passed directory name
    return _find_files(suffix, path, files)

########## TESTING ##########

# all files with suffix .c in subdirectory p2_testdir/
print()
print("all files with suffix .c in subdirectory p2_testdir/")
print(*find_files(".c", "p2_testdir"), sep = "\n")
# p2_testdir/t1.c
# p2_testdir/subdir5/a.c
# p2_testdir/subdir3/subsubdir1/b.c
# p2_testdir/subdir1/a.c

# all files with suffix .h in subdirectory p2_testdir/
print()
print("all files with suffix .h in subdirectory p2_testdir/")
print(*find_files(".h", "p2_testdir"), sep = "\n")
# p2_testdir/t1.h
# p2_testdir/subdir5/a.h
# p2_testdir/subdir3/subsubdir1/b.h
# p2_testdir/subdir1/a.h

# all files with suffix .py in current directory ./
print()
print("all files with suffix .py in current directory ./")
print(*find_files(".py", "."), sep = "\n")
# ./problem_2.py
# ./problem_1.py

# all files with suffix .none in current directory ./
print()
print("all files with suffix .none in current directory ./")
print(*find_files(".none", "."), sep = "\n")
# (no output)
