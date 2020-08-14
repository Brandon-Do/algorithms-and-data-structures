import heapq
from common import get_random_ints

def get_children_indicies(nums: list, i: int):
  left = (2 * (i+1)) - 1
  right = left + 1
  return left, right


def is_leaf(nums: list, i: int):
  left, right = get_children_indicies(nums, i)
  return left >= len(nums)


def min_heapify(nums: list, i = 0):  
  if i >= len(nums) or is_leaf(nums, i):
    return
  
  left, right = get_children_indicies(nums, i)

  min_heapify(nums, left)
  min_heapify(nums, right)

  left_val = nums[left] if left < len(nums) else float('inf')
  right_val = nums[right] if right < len(nums) else float('inf')

  vals = [(left_val, left), (right_val, right)]
  vals.sort()
  
  child_min_val, child_min_val_i = vals[0]

  if child_min_val < nums[i]:
    nums[i], nums[child_min_val_i] = nums[child_min_val_i], nums[i]




if __name__ == "__main__":
    nums = get_random_ints(20, 0, 9)
    copy = [n for n in nums]

    min_heap = min_heapify(nums)
    heapq.heapify(copy)

    res_one = []
    while nums:
      res_one.append(heapq.heappop(nums))

    res_two = []
    while copy:
      res_two.append(heapq.heappop(copy))

    print(res_one)
    print(res_two)
    
    