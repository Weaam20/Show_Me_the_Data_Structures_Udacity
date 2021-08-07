class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(list_1, list_2):
    """
    This method will returns the set of elements which are in either list
    :param list_2: first linkedList
    :param list_1: second LinkedList
    :return: Union LinkedList
    """
    # if both lists was empty.
    if list_1.size() == 0 and list_2.size() == 0:
        return None
    # if the first LinkedList is empty or the second.
    if list_1.size() == 0:
        return list_2
    elif list_2.size() == 0:
        return list_1

    set_union = set()

    # Add all values of first LinkedList to set.
    curr = list_1.head
    while curr.next is not None:
        set_union.add(curr.value)
        curr = curr.next

    # Add all values of second LinkedList to set.
    curr = list_2.head
    while curr.next is not None:
        set_union.add(curr.value)
        curr = curr.next

    # Add all elements of the set in Union LinkedList.
    Union = LinkedList()
    for item in set_union:
        Union.append(item)

    return Union


def intersection(list_1, list_2):
    """
    this method will returns the set of elements which are in both lists
    :param list_2: first linkedList
    :param list_1: second LinkedList
    :return: Intersection LinkedList
    """
    # if both lists was empty or if the first LinkedList is empty or the second.
    if (list_1.size() == 0 and list_2.size() == 0) or list_1.size() == 0 or list_2.size() == 0:
        return None

    intersection_set = set()
    set_ = set()

    # Add all elements of list_2 in list_3
    curr = list_2.head
    while curr is not None:
        set_.add(curr.value)
        curr = curr.next

    # Add all elements that in the first LinkedList and in the second LinkedList.
    curr = list_1.head
    while curr is not None:
        if curr.value in set_:
            intersection_set.add(curr.value)
        curr = curr.next

    # Add all intersection elements that exist in the first LinkedList and in the second LinkedList to intersection_set.
    new_linked_list = LinkedList()
    for item in intersection_set:
        new_linked_list.append(item)

    return new_linked_list


# Test case 1 ------------------------------------------------------------
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('Union: ', union(linked_list_1, linked_list_2))
print('intersection: ', intersection(linked_list_1, linked_list_2))
print('---------------------------------')

# Test case 2 ------------------------------------------------------------

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('Union: ', union(linked_list_3, linked_list_4))
print('intersection: ', intersection(linked_list_3, linked_list_4))
print('---------------------------------')

# Test case 3 ------------------------------------------------------------

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print('Union: ', union(linked_list_6, linked_list_5))
print('intersection: ', intersection(linked_list_5, linked_list_6))
print('---------------------------------')

# Test case 4 ------------------------------------------------------------

element_2 = [10, 70, 8, 99, 11, 21, 1]

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

for i in element_1:
    linked_list_7.append(i)

print('Union: ', union(linked_list_7, linked_list_8))
print('intersection: ', intersection(linked_list_7, linked_list_8))
print('---------------------------------')

# Test case 5 ------------------------------------------------------------
element_1 = [33, 26, 48, 35, 68, 65, 67, 40, 3, 23]

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

for i in element_2:
    linked_list_10.append(i)

print('Union: ', union(linked_list_9, linked_list_10))
print('intersection: ', intersection(linked_list_9, linked_list_10))
print('---------------------------------')
