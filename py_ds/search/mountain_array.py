"""
A mountain array is an array which satisifes these properties:
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