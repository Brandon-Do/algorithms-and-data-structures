from common import get_random_ints
from collections import Counter


if __name__ == "__main__":
    nums = get_random_ints(10000, lower_bound = 0, upper_bound = 9)
    counter = Counter(nums)
    print(counter)

    nums = get_random_ints(10000, lower_bound = 0, upper_bound = 9)
    nums_str = ''.join([str(n) for n in nums])
    counter = Counter(nums_str)
    print(counter)

"""
Output:
  Counter({9: 1040, 5: 1030, 6: 1029, 8: 1002, 1: 999, 7: 998, 2: 994, 0: 976, 4: 967, 3: 965})
  Counter({'6': 1030, '5': 1012, '8': 1006, '4': 1005, '7': 1002, '9': 1001, '2': 996, '0': 995, '3': 984, '1': 969})
"""