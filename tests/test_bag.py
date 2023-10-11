import pytest

from py_ds.adt.bag import Bag


@pytest.fixture()
def empty_bag():
    '''Returns an empty Bag'''
    return Bag()


@pytest.fixture()
def bag_with_singleton():
    '''Returns a Bag containing excatly this item'''
    return Bag(1)


@pytest.fixture()
def bag_with_items():
    '''Returns a Bag containing some items'''
    return Bag(1, 2.345, "foo", "bar", False)


def test_empty_bag_should_contain_nothing(empty_bag):
    assert empty_bag.__len__() == 0
    assert empty_bag.__contains__(None) == False


def test_nonempty_bag_should_contain_item(bag_with_singleton):
    assert bag_with_singleton.__len__() == 1
    assert bag_with_singleton.__contains__(1)


def test_bags_with_items_can_be_iterated_over(bag_with_items):
    assert bag_with_items.__len__() == 5
    idx = 0
    for item in bag_with_items:
        assert item != None
        idx += 1
    assert idx == 5

def test_bags_can_be_extended(bag_with_singleton):
    x = 1.23456789
    bag_with_singleton.add(x)
    assert bag_with_singleton.__contains__(x)
    assert bag_with_singleton.__len__() == 2

def test_bags_can_be_shrunk(bag_with_singleton):
    bag_with_singleton.remove(1)
    assert not bag_with_singleton.__contains__(1)
    assert bag_with_singleton.__len__() == 0
    with pytest.raises(AssertionError):
        bag_with_singleton.remove(1) # no longer in the bag

def test_bag_iterator(bag_with_items):
    just_integers = list(filter(lambda x: type(x) == int, bag_with_items.__iter__()))
    assert just_integers == [1]
    just_booleans = list(filter(lambda x: type(x) == bool, bag_with_items.__iter__()))
    assert just_booleans == [False]