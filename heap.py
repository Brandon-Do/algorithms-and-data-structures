from common import get_random_ints
from heapq import heappop, heappush, heapify


""" 
Testing to see if heapify operations
  sorts on characters
>>> [('a', 0), ('a', 1), ('a', 2), ('b', 3), ('b', 4), ('b', 5)]
"""
def test_heap_order_with_chars():
  letters = ['a' for _ in range(3)] + ['b' for _ in range(3)]
  letters = [(l, i) for i, l in enumerate(letters)]
  heapify(letters)
  res = []

  while letters:
    res.append(heappop(letters))
  
  print(res)


"""
Testing to see if the heapify operation
  sorts based on secondary indicies
"""
def test_heap_order_with_tuples():
  nums = get_random_ints(100, 0, 1)
  nums_with_inds = [(n, i) for i, n in enumerate(nums)]
  heapify(nums_with_inds)
  
  res = []
  while nums_with_inds:
    res.append(heappop(nums_with_inds))
  
  print(res)


if __name__ == "__main__":    
    test_heap_order_with_chars()
    test_heap_order_with_tuples()