"""
Problem 4: Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves.

We can construct this hierarchy as such. Whre User is represented by str representing their ids
"""
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

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    result = False
    user_list = group.get_users()
    # print(user_list)
    if user in user_list:
        result = True

    else:
        group_list = group.get_groups()
        for group in group_list:
            result = is_user_in_group(user, group)
            if result:
                return result


    return result

### TEST CASES ###

# Case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))
print(is_user_in_group("sub_child_user", child))
print(is_user_in_group("sub_child_user", sub_child))

# Expected results:
# True
# True
# True

# Case 2
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))
print(is_user_in_group("sub_child_user", child))
print(is_user_in_group("sub_child_user", sub_child))

# Expected results:
# False
# False
# False

# Case 3

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("child_user", parent))
print(is_user_in_group("child_user", child))
print(is_user_in_group("child_user", sub_child))

# Expected results:
# True
# True
# False