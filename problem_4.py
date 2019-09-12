class Group:

    # group has a name, users, and children groups
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.users = []

    # simple getters and setters
    def get_name(self):
        return self.name
    def get_groups(self):
        return self.groups
    def get_users(self):
        return self.users
    def add_group(self, group):
        self.groups.append(group)
    def add_user(self, user):
        self.users.append(user)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # initialize a blank list for output
    users = []

    # recursive function to collect all users in passed group
    def get_all_users(group):

        # add the users on this group level
        users.extend(group.get_users())

        # get the subgroup children of this group
        groups = group.get_groups()

        # base case, there are no subgroups and we are at the lowest level
        if len(groups) == 0:
            return users

        # subgroups exist, recurse into each one
        for group in groups:
            get_all_users(group)

        return users

    # start recursion
    users = get_all_users(group)

    # search through the all collected users
    for _user in users:

        # current user matches passed user
        if user == _user:
            return True

    return False

########## TESTING ##########

# create a few groups
parent_group = Group("parent_group")
child_1_group = Group("child_1_group")
child_2_group = Group("child_2_group")
sub_child_1_group = Group("sub_child_1_group")

# define the group heirarchy
parent_group.add_group(child_1_group)
parent_group.add_group(child_2_group)
child_1_group.add_group(sub_child_1_group)

# add a user to each group level
parent_group.add_user("parent_user")
child_1_group.add_user("child_1_user")
child_2_group.add_user("child_2_user")
sub_child_1_group.add_user("sub_child_1_user")

# check for the presence of the sub_child_1_user in its native sub_child_1_group
print(is_user_in_group("sub_child_1_user", sub_child_1_group))
# True

# the sub_child_1_user is also a member of the parent group
print(is_user_in_group("sub_child_1_user", parent_group))
# True

# check for the presence of a nonexistant user
print(is_user_in_group("non_existant_user", child_1_group))
# False

# verify the presence of the parent_user in the top level parent_group
print(is_user_in_group("parent_user", parent_group))
# True

# edge case: empty user name string
print(is_user_in_group("", parent_group))
# False
