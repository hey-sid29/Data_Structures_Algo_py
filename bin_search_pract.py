"""Question: Given an array in increasing order of elements find out the first index and last index of a queried 
number."""


def binary_search(lo, hi, condition):
    mid = (lo+hi) // 2
    result = condition(mid)
    if result == 'found':
        return mid
    elif result == 'left':
        hi= mid-1
    else:
        lo = mid+1
    return -1



def first_index(arr, target):
  def condition_first(mid):
    if arr[mid] == target:
        if mid>0 and arr[mid-1] == target:
          return 'left'
        return 'found'
    elif arr[mid]<target:
        return 'right'
    else:
        return 'left'
  return binary_search(0, len(arr)-1, condition_first)


def last_index(arr, target):
    def condition_last(mid):
     if arr[mid] == target:
        if mid<len(arr)-1 and arr[mid+1] == target:
            return 'right'
        return 'found'
     elif arr[mid]<target:
        return 'right'
     else:
        return 'left'
