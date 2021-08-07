class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        if user == '' or user is None:
            print('please enter a valid name!')
            return
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

    if user in group.get_users():
        return True
    else:
        sub_groups = group.get_groups()
        if len(sub_groups) == 0:
            return False
        else:
            for sub_group in sub_groups:
                return is_user_in_group(user, sub_group)

    return False


# Test
parent = Group("parent")
child = Group("child")
sub_child = Group("sub child")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group('sub_child_user', parent))


print(is_user_in_group('Amal', parent))  # return false
Cs = Group('Computer Science Department')
Cs.add_user("Amal")
sub_child.add_group(Cs)
print(is_user_in_group('Amal', parent))  # return True

# -------------------------------------------------------- invalid inputs
Cs.add_user('')  # return 'pleas enter a valid name!'
Cs.add_user(None)  # return 'pleas enter a valid name!'
