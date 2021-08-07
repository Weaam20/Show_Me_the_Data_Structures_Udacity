import os


def find_files(suffix, path):
    """
    :param suffix: suffix if the file name to be found
    :param path: path of the file system
    :return: a list of paths
    """

    if path == '' or path is None:
        print('Invalid path')
        return None

    elif not os.path.isdir(path):
        print('This path is not for an existing file.')
        return None

    return find_files_2(suffix, path, set(), [])


def find_files_2(suffix, path, visited, list_paths):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
     :param path: path of the file system
     :param suffix: suffix if the file name to be found
     :param list_paths: is a list contains paths end with specific suffix.
     :param visited: is a list contains all visited paths

    Returns: a list of paths
    """

    # if path end with specific suffix
    if suffix == '.'+(path.split('.')[-1]):
        list_paths.append(path)
        return list_paths
    # if the path have children
    if os.path.isdir(path):
        dir_paths = os.listdir(path)
    else:
        return list_paths
    # add path to visited list
    visited.add(path)

    # go deep of the path to search
    for child in dir_paths:
        if child not in visited:
            items = find_files_2(suffix, path+'/'+child, visited, list_paths)
            if items is not None:
                list_paths = items

    return list_paths


# Test case 1
print(find_files('.c', 'testdir'))
print('---------------------------------')

# Test case 2
print(find_files('.c', 'read'))
print('---------------------------------')

# Test case 3
print(find_files('.c', ''))
print('---------------------------------')
