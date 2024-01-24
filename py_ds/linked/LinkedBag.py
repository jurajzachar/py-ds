class LinkedBag:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, item):
        cur_node = self._head
        while cur_node is not None and cur_node.item != item:
            cur_node = cur_node.next
        return cur_node is not None

    # adds a new item to the linked bag
    def add(self, item):
        new_node = _LinkedBagNode(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    # removes an instance of the item from the bag
    def remove(self, item):
        prev_node = None
        cur_node = self._head
        # this is the same as __contains__ traversal
        while cur_node is not None and cur_node.item != item:
            prev_node = cur_node
            cur_node = cur_node.next

        assert cur_node is not None, "The item must be in the bag."

        # unlink the node in the bag to remove it
        if cur_node is self._head:
            self._head = cur_node.next
        else:
            prev_node.next = cur_node.next
        self._size -= 1
        return cur_node.item

    def __iter__(self):
        from py_ds.adt.bag import _BagIterator
        return _BagIterator(self._head)

# Defines a private storage class for creating linked nodes
class _LinkedBagNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None