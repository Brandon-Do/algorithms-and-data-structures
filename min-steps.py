def get_min_steps(n: int) -> int:
  steps = [0] + [float('inf') for _ in range(n-1)]

  for step in range(n):
    for next_step in (step+1, step*2, step*3):
      if next_step >= n: continue
      steps[next_step] = min(steps[next_step], steps[step] + 1)

  return steps[-1] 


if __name__ == "__main__":
    result = get_min_steps(10000)
    print(result)