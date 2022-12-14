#init memoization table
memo_table = {}

def calc_tilling_ways(grid):
  #cache hits
  grid_hash = hash_grid(grid)
  memoization_result = memo_table.get(grid_hash)
  if memoization_result: return memoization_result

  #get the target line and its size
  max_line_size = max(grid)
  if max_line_size <= 1:
    return 1

  #find the target line index
  target_index = grid.index(max_line_size)

  #find the max square that can be removed at target position
  max_square_size = 1
  for line_size in grid[target_index+1:]:
    #max square size reached condition
    if line_size < max_line_size or max_square_size == line_size:
      break
    max_square_size += 1

  #remove every possible square and calculate the ways of tilling
  ways_of_tilling = 0
  for square_size in range(1, max_square_size+1):
    new_grid = remove_square(grid, square_size, target_index)
    ways_of_tilling += calc_tilling_ways(new_grid)

  memo_table[grid_hash] = ways_of_tilling
  return ways_of_tilling
  
def remove_square(grid, square_size, target_index):
  new_grid = [*grid] #copy grid
  for i in range(target_index, target_index+square_size):
    new_value = new_grid[i] - square_size
    new_grid[i] = new_value if new_value > 1 else 0
  return new_grid

def hash_grid(grid):
  return hash(tuple(grid))

def print_grid(grid):
  for line_size in grid:
    print("1"*line_size)
  print()

def main():
  grid_height = int(input())
  input() #we don't care about the grid width
  
  grid = []
  for _ in range(grid_height):
    line_size = int(input())
    grid.append(line_size)

  print(calc_tilling_ways(grid) if max(grid) else 0)

if __name__ == "__main__":
  main() 