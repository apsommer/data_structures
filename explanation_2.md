# File Recursion

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing:

```
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h

```

Python's os module will be useful—in particular, you may want to use the following resources:

[os.path.isdir(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isdir)

[os.path.isfile(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isfile)

[os.listdir(directory)](https://docs.python.org/3.7/library/os.html#os.listdir)

[os.path.join(...)](https://docs.python.org/3.7/library/os.path.html#os.path.join)

Note: `os.walk()` is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use `os.walk()`.

### Solution

problem_2.py

### Explanation

The data structure for this problem is explicitly defined in the problem statement: return a list. No other structures are necessary. Another perspective on this solution is to consider this as traversal through a tree structure. The leaves of the tree are the files, and the directories are nodes.

The time complexity is O(n), where n = number of items, both files and directories, in the passed input "path" directory. Since this is a recursive search algorithm through an unordered, unknown directory structure, the best, average, and worst cases are all the same at O(n). We need to search everything to check if the entity has the suffix of interest, there is no further optimization in this case.

Space complexity is more difficult to calculate as this algorithm uses recursion. All constant input complexity for the function is required each time another instance is recursively added to the call stack. This includes the expanding list of suffix matches. The call stack size requirement can be approximated by how many times the function is recursively called, which in this case is once for every subdirectory in the path. Let d = total number of directories in the path, then total space = d * n, where n is the list of suffix matches and other local variables. Even though n changes on each level, we can say that the total number of calls added to the stack is proportional to the number of directories, d. Therefore, space complexity reduces to O(n), where n = d = number of directories in the path.
