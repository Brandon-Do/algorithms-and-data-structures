import random


def get_random_ints(count: int, lower_bound = 0, upper_bound = 10000) -> list:
  return [random.randint(lower_bound, upper_bound) for _ in range(count)]


if __name__ == "__main__":
    pass