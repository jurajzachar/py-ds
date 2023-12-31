# Implements the Bag ADT container using a Python list.
class Bag:

    # Constructs an empty bag.
    def __init__(self):
        self._theItems = []

    # Constructs a singleton bag.
    def __init__(self, item):
        self._theItems = []
        self.add(item)

        # Constructs a singleton bag.

    def __init__(self, *items):
        self._theItems = []
        for item in items:
            self.add(item)

    # Returns the number of items in the bag.
    def __len__(self):
        return len(self._theItems)

    # Determines if an item is contained in the bag.
    def __contains__(self, item):
        return item in self._theItems

    # Adds a new item to the bag.
    def add(self, item):
        self._theItems.append(item)

    # Removes and returns an instance of the item from the bag.
    def remove(self, item):
        assert item in self._theItems, "The item must be in the bag."
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _BagIterator(self._theItems)


class _BagIterator:
    def __init__(self, theArr):
        self._bagItems = theArr
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
