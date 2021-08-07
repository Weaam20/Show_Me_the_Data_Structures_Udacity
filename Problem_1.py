from Double_linked_list import DoublyLinkedList
import sys


class LruCache(object):

    def __init__(self, capacity):
        """
        :param capacity: is a capacity of our cache

        NOTE: here we will initials our cache: we use a double linked list in this problem because we want fast
        operation on delete and insert elements O(1).And dictionary for keep track of reference of the node to access
        in O(1) we do not have to search inside the double linked list.

        """
        self.hash = {}
        self.LRU = DoublyLinkedList()
        if capacity is not None and sys.maxsize > capacity > 0:
            self.capacity = capacity
        else:
            return

    # start method remove_at(key)
    def remove_at(self, key):
        """
        :param key: is the key of the node and we use it to remove a specific node in LRU.
        :return: the value of removed item.
        """

        # if LRU is empty we don't have to delete any things.
        if self.LRU.is_empty():
            return -1
        # tack the reference of the node that have key value from hash(our dictionary).
        item = self.hash.get(key)
        # if we don't find any node that have key value.
        if item is None:
            return -1
        """
        delete the reference of the node that has a key-value from a hash(our dictionary) because we don't need this
        reference anymore.
        """
        del self.hash[key]
        # if this node is refer to the tail then use method remove from the tail then return.
        if item is self.LRU.tail:
            element = self.LRU.remove_last()
            return element

        # remove the node that has a key value
        if item.previous is not None:
            item.previous.next = item.next
        if item.next is not None:
            item.next.previous = item.previous

        self.LRU.elements -= 1
        return item.data

    # end method remove_at(key)

    # start method get(self, key)
    def get(self, key):
        """
        :param key: is the key of the node and we use it to remove a specific node in LRU.
        :return: the value of the item we looking for.
        """
        # tack the reference of the node that has a key value from a hash(our dictionary).
        item = self.hash.get(key)
        # if we don't find any node that has a key value.
        if item is None:
            return -1
        # remove this node and then add it in the first LRU.
        self.remove_at(key)
        self.LRU.add_first(key, item)
        # update the reference of this node with the new one.
        self.hash.update({key: self.LRU.head})
        return item.data

    # end method get(self, key)

    # start methode print()
    def print(self):
        """
        this method for print items and size of LRU.
        """

        if not hasattr(self, 'capacity'):
            print('This object has not attribute capacity')
            return

        curr = self.LRU.head
        print('Inside LRU: ')
        while curr is not None:
            print(curr.data)
            curr = curr.next

        print('---------------')
        print('Size: ', our_cache.LRU.size())
        print('---------------')

    # end methode print()

    # start methode set(self, key, value)
    def set(self, key, value):
        """
        :param key: is the key of the node and we use it to put new node in LRU.
        :param value: is the value of the node and we use it to put new node in LRU.
        :return: nothing
        """

        if not hasattr(self, 'capacity'):
            print('This object has not attribute capacity')
            return

        if key is None or key == '' or key >= sys.maxsize or value is None or value == '' or value >= sys.maxsize:
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.LRU.size() == self.capacity:
            del self.hash[self.LRU.tail.key]
            self.LRU.remove_last()
        self.LRU.add_first(key, value)
        # add new reference in hash(our dictionary).
        self.hash.update({key: self.LRU.head})
    # end methode set(self, key, value)


# --------------------------------------- Test
our_cache = LruCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.print()

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.print()

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.print()

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))

# all these operation our_cache.set( key, value) are not valid in our_cache we will reject all of them.
our_cache.set('', 8)
our_cache.print()

our_cache.set(None, 7)
our_cache.print()

our_cache.set(sys.maxsize, 9)
our_cache.print()

our_cache.set(2, None)
our_cache.print()

our_cache.set(5, sys.maxsize)
our_cache.print()

our_cache.set(4, '')
our_cache.print()

# ---------------------------- invalid LRU
our_cache_2 = LruCache(0)
our_cache_2.print()  # will return 'This object has not attribute capacity'

our_cache_2.set(6, 6)  # will return 'This object has not attribute capacity'
our_cache_2.print()   # will return 'This object has not attribute capacity'


our_cache_2 = LruCache(None)
our_cache_2.print()  # will return 'This object has not attribute capacity'

our_cache_2.set(6, 6)  # will return 'This object has not attribute capacity'
our_cache_2.print()  # will return 'This object has not attribute capacity'

our_cache_2 = LruCache(sys.maxsize)
our_cache_2.print()  # will return 'This object has not attribute capacity'

our_cache_2.set(6, 6)  # will return 'This object has not attribute capacity'
our_cache_2.print()  # will return 'This object has not attribute capacity'


our_cache_2 = LruCache(-1)
our_cache_2.print()  # will return 'This object has not attribute capacity'

our_cache_2.set(6, 6)  # will return 'This object has not attribute capacity'
our_cache_2.print()  # will return 'This object has not attribute capacity'
