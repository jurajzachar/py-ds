import pytest

from py_ds.linked.LinkedBag import LinkedBag


@pytest.fixture
def empty_bag():
    '''Returns an empty Bag'''
    return LinkedBag()

def test_empty_bag_should_contain_nothing(empty_bag):
    assert empty_bag.__len__() == 0

def test_add(empty_bag):
    empty_bag.add("some string")
    assert empty_bag.__contains__("some string")
    empty_bag.add(1)
    assert empty_bag.__contains__("some string")
    assert empty_bag.__contains__(1)


def test_remove(empty_bag):
    item = dict(first_attr=1, second_attr=2)
    keeper = [1,2,4,5,6]
    empty_bag.add(item)
    empty_bag.add(keeper)
    empty_bag.remove(item)
    assert empty_bag.__contains__(keeper)
    assert not empty_bag.__contains__(item)

