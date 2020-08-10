from common import get_random_ints

"""
  Looking to see how the built-in python .sort function sorts
  lists of numbers.

  It appears that it sorts lists based on all values, where the
  lowest indicies take highest priority in the sorting.

  Python's built in uses TimSort, with worstcase time complexity O(nlogn)
  and best case O(n), where worst case memory is O(n)

  This is because TimSort is an algorithm that is a combination of merge sort
  and insertion sort
"""
if __name__ == "__main__":
  list_count = 10
  lists = [get_random_ints(5, lower_bound = 1, upper_bound = 2) for _ in range(list_count)]

  for l in lists:
    l[0] = 0

  lists.sort()
  
  for i, l in enumerate(lists):
    print('%s:' % i, l)