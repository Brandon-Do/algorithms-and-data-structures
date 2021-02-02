"""
Demonstrates a dynamic-programming solution to the
0/1 knapsack problem.

Example items:

weight | value
1        20
2        25
3        35

The recurrence relationship is:
  V[i][w] = max(V[i-1][w], V[i-1][w-weight[i]] + value[i]) if weight[i] <= w
            else V[i-1][w]

We're building up from the top row down to the bottom. For each row, we get the
  max value at each possible weight. Then our option is:
    1. Take the current item + the maximum value from the remaining weight
    2. Do not take the current item

Example if our maximum weight was 4

    0   1   2   3   4
1   0   20  20  20  20  <--- Only know about item 1
2   0   20  25  45  45  <--- Know about items 1 and 2
3   0   20  25  45  55  <--- Know about all items, 
                              the last takes item 3 and 1
"""
class Solution():
  def __init__(self):
    self.matrix = []

  def get_max_value_knapsack(self, max_weight, weights, values):
    if not max_weight:
      return 0

    n = len(weights)
    self.matrix = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for row_index in range(1, n + 1):
      weight = weights[row_index-1]
      value = values[row_index-1]

      for col_index in range(max_weight + 1):
        leave_item = self.matrix[row_index-1][col_index]
        take_item = self.matrix[row_index-1][col_index-weight] + value

        self.matrix[row_index][col_index] = max(take_item, leave_item) if weight <= col_index \
                                                                       else leave_item
    return self.matrix[-1][-1]

  """ For debugging purposes """
  def print_matrix(self):
    for row in self.matrix:
      print(row)

if __name__ == '__main__':
  solution = Solution()

  answer = solution.get_max_value_knapsack(
    max_weight=4,
    weights=[1, 2, 3],
    values=[20, 25, 35]
  )
  solution.print_matrix()
  print(answer)
  # [0, 0, 0, 0, 0]
  # [0, 20, 20, 20, 20]
  # [0, 20, 25, 45, 45]
  # [0, 20, 25, 45, 55]
  # 55

  answer = solution.get_max_value_knapsack(
    max_weight=5,
    weights=[5, 3, 4, 2],
    values=[60, 50, 70, 30]
  )
  solution.print_matrix()
  print(answer)
  # [0, 0, 0, 0, 0, 0]
  # [0, 0, 0, 0, 0, 60]
  # [0, 0, 0, 50, 50, 60]
  # [0, 0, 0, 50, 70, 70]
  # [0, 0, 30, 50, 70, 80]
  # 80