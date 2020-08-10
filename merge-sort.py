"""
  Implemented merge sort here
  Time: O(nlogn) -- scan the array each split
  Space: O(n) -- need to hold a copy of the array in memory
"""
def merge_sort(nums: list) -> list:
  if len(nums) <= 1:
    return nums

  mid = len(nums) // 2
  first_half = merge_sort(nums[:mid])
  second_half = merge_sort(nums[mid:])

  return merge(first_half, second_half)


def merge(first_half: list, second_half: list) -> list:
  if not (first_half or second_half): 
    return [] # both lists are empty

  results = []
  i, j = 0, 0

  while i < len(first_half) and j < len(second_half):
    if first_half[i] < second_half[j]:
      results.append(first_half[i])
      i += 1
    else:
      results.append(second_half[j])
      j += 1
  
  if i < len(first_half):
    results += first_half[i:]
  elif j < len(second_half):
    results += second_half[j:]
  
  return results


if __name__ == "__main__":
  numbers = get_random_ints(20)
  print(numbers)
  sorted_numbers = merge_sort(numbers)
  print(sorted_numbers)