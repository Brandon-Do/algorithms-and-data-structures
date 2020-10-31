from collections import deque
from common import get_random_ints


def main():
  min_deque = deque()
  for number in get_random_ints(20, 0, 10):
    while min_deque and number <= min_deque[-1]:
      print('Removed:', min_deque.pop(), 'from min deque')
    min_deque.append(number)
    print(min_deque)


if __name__ == "__main__":
    main()