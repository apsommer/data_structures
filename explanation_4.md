# Windows Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

```
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

```
Write a function that provides an efficient look up of whether the user is in a group.

```
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return None
```

### Solution

problem_4.py

### Explanation

This algorithm uses the array data structure. Each array can hold simple strings, or other nested arrays. For this function the entire nested array configuration must be searched for a given user, resulting in O(n), where n is the total number of users in the entire hierarchy.

One alternative would be to maintain a hashmap of users independent of the group hierarchy structure, therefore get() and set() against a specific username would be O(1). This of course increases space complexity as we now have the nested array structure and the hashmap to maintain. The user's position in the group hierarchy could also included in the each hashmap entry, however this is an awkward way to reference a tree-like structure. If search speed is critical, then space and clarity may be sacrificed in this way.

Space complexity analysis of an algorithm that uses recursion must consider that all input complexity such as local variable and input parameters will be added to the call stack each time the function is recursively called. Let g = number of subgroups in the passed group, then the number of allocations on the call stack can be approximated as O(g). Therefore set n = g to use common nomenclature, and space complexity is written as O(n).
