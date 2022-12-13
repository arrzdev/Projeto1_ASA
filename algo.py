#memoization table
memo = {}

def solution(grid):
  #max column
  target_line_size = max(grid)
  if target_line_size <= 1:
    return 1

  #cache hits
  grid_hash = hash_grid(grid)
  memo_result = memo.get(grid_hash)
  if memo_result: return memo_result
  
  target_index = grid.index(target_line_size)

  #find the max square that can be removed
  segment_size = 1
  for line_size in grid[target_index+1:]:
    #max segment_size reached
    if line_size < target_line_size or segment_size == line_size:
      break
    segment_size += 1

  #remove it
  ways_of_tilling = 0
  for square_size in range(1, segment_size+1):
    new_grid = remove_square(grid, square_size, target_index)
    ways_of_tilling += solution(new_grid)

  memo[grid_hash] = ways_of_tilling
  return ways_of_tilling
  
def remove_square(grid, square_size, target_index):
  new_grid = [*grid]
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
  
  has_content = 0
  grid = []
  for _ in range(grid_height):
    line_size = int(input())
    if line_size:
      has_content = 1
    if line_size > 1:
      grid.append(line_size)

  print(solution(grid) if len(grid) else has_content)

if __name__ == "__main__":
  main() 