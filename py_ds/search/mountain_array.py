"""
A mountain array is an array which satisfies these properties:
  * arr.length >= 3
  * there existing some 'i' with 0 < i < arr.length -1 such that:
    * arr[0] < arr[1] < ... < arr[i-1] < arr[i] ==> (left-hand side is sorted in ascending order)
    * arr[i] > arr[i+1] > ... arr[arr.length -1] ==> (right-hand side is sorted in descending order)
  * "mountain peak" is the highest element of the array

an example of a mountain array: [1,2,3,4,5,3,1]

q: Given a mountain array mountainArr, return the minimum 'index' such that mountainArr.get(index) == target.
You cannot access the array directly, you may only access it using a 'MountainArray' interface comprising:
  * MountainArray.get(k) ==> returns the element of the array at index 'k' (0-indexed)
  * MountainArray.length() ==> return the length of the array

"""

from array import array


class MountainArray():
    def __init__(self, elems: [], type_code='i', ) -> None:
        """initializes an empty MountainArray for the given type and elements"""
        if len(elems) < 3:
            raise RuntimeError('A MountainArray must contain at least 3 elements')
        self.__type_code = type_code
        self.__array = array(type_code, elems)
        self.__sort()

    def get(self, index: int):
        """returns element at the index or None otherwise"""
        try:
            return self.__array[index]
        except IndexError:
            return None

    def __sort(self) -> None:
        """sort left and right branches of this array"""
        left = array(self.__type_code, [])
        right = []  # list will be sorted in desc order and converted back to an array at the end
        tmp_list = self.__array.tolist()
        tmp_list.sort()
        # populate left side
        previous = None
        for x in tmp_list:
            if previous is None:
                left.append(x)
            elif previous is not None and x > previous:
                left.append(x)
            elif previous is not None and x == previous:
                right.append(x)
            previous = x
        # right side needs sorting in rever order
        right.sort(reverse=True)
        # merge
        left.extend(array(self.__type_code, right))
        # re-assign to protected var
        self.__array = left

    def length(self):
        return len(self.__array)

    def toList(self) -> []:
        return self.__array.tolist()


class Solution():
    def findMinimumIndex(self, target: int, mountain_arr: MountainArray) -> int:
        length = mountain_arr.length()

        # find peak
        _left, _right = 1, length - 2  # because we know the peak is never at the edges
        while _left <= _right:
            _middle = (_left + _right) // 2
            left, middle, right = mountain_arr.get(_middle - 1), mountain_arr.get(_middle), mountain_arr.get(
                _middle + 1)
            if left < middle < right:
                _left = _middle + 1
            elif left > middle > right:
                _right = _middle - 1
            else:
                break # found
        peak = middle

        # search left portion
        _left, _right = 0, peak
        while _left <= _right:
            _middle = (_left + _right) // 2
            val = mountain_arr.get(_middle)
            if val < target:
                _left = _middle + 1
            elif val > target:
                _right = _middle - 1
            else:
                return _middle  # found

        # search right portion
        _left, _right = peak, length - 1
        while _left <= _right:
            _middle = (_left + _right) // 2
            val = mountain_arr.get(_middle)
            if val > target:
                _left = _middle + 1
            elif val < target:
                _right = _middle - 1
            else:
                return _middle  # found

        # element not found
        return -1
