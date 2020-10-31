"""
This is pseudo code to model a backtracking solution.

Backtracking is an optimization when finding all possibilities.
  This is opposed to finding all possible combinations O(n^n).
  Backtracking has a time complexity of O(n!)

Imagine a decision tree, we start from nothing and try all possibilities that are valid.
   If the current state is not valid, we do not continue.
   This trims off sections of the decision tree.
"""

def backtrack(candidate):
  # the assumption is that the candidate is valid
  if found_answer(candidate):
    output_answer(candidate)
    return

  for next_candidate in next_candidates:
    if not valid(next_candidate):
      continue # do not do recursion when the candidate is invald
    
    # Place the next candidate
    place(next_candidate)

    # Then move forward with the next candidate 
    # as the candidate and select ones available
    backtrack(next_candidate)

    # Undo the candidate to try other possibilities
    remove(next_candidate)