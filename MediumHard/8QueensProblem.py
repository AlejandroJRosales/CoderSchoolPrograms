import random

def show(soln, n):
  """
  This displays the board
  """
  for i in range(n):
    row = ['[]'] * n
    for col in range(n):
      if soln[col] == n - 1 - i:
        row[col] = 'Q '
    print(''.join(row))

def min_conflicts(soln, n, iters=1000):
  """
  This is where the magic happens
  """
  def random_pos(li, filt):
    """
    This feels the board with queens at random positions
    """
    return random.choice([i for i in range(n) if filt(li[i])])

  for k in range(iters):
    print("\n\n")
    conflicts = find_conflicts(soln, n)
    # This checks to see if there are no conflicts, if true where done and return the final board
    if sum(conflicts) == 0:
      return soln
    col = random_pos(conflicts, lambda elt: elt > 0)
    vconflicts = [hits(soln, n, col, row) for row in range(n)]
    # Prints our each board position
    show(soln, n)
    soln[col] = random_pos(vconflicts, lambda elt: elt == min(vconflicts))
  # If we run out of iterations than we say that we could not complete the solution with the given iterations
  raise Exception("Incomplete solution: try more iterations.")

def find_conflicts(soln, n):
  """
  This part returns a list of all the conflicts currently with the board
  """
  return [hits(soln, n, col, soln[col]) for col in range(n)]

def hits(soln, n, col, row):
  """
  This part finds all the hits that exist in a given column
  """
  total = 0
  for i in range(n):
    if i == col:
      continue
    if soln[i] == row or abs(i - col) == abs(soln[i] - row):
      total += 1
  return total

def nqueens(n):
  # Shows the board solution
  show(min_conflicts(list(range(n)), n), n)

def main():
  # This initiates the whole thing
  nqueens(8)

if __name__ == '__main__':
  main()
