import time

def solution(matrix):
  n_lines = len(matrix)
  if n_lines <= 1:
    return 1

  line = matrix[0]
  if "11" not in line:
    return solution(matrix[1:])

  matrix_hash = hash_matrix(matrix)
  memoization_result = memoization_table.get(matrix_hash)
  if memoization_result:
    return memoization_result

  #get first content value
  n_entry = line.index("1")

  #get the max square size
  ending_search_index = line.find("0", n_entry) if "0" in line[n_entry:] else n_entry + n_lines
  segment_size = line[n_entry:ending_search_index].count("1")

  #calc the max square size that can be removed at position n_entry
  square_size = min(segment_size, n_lines)

  ways_of_tilling = 0
  for n_size in range(1, square_size+1):
    new_matrix = remove_square(matrix, n_size, n_entry)
    ways_of_tilling += solution(new_matrix)
  
  memoization_table[matrix_hash] = ways_of_tilling
  return ways_of_tilling

def remove_square(matrix, square_size, n_entry):
  new_matrix = [*matrix]
  for n_line in range(square_size):
    line_to_update = new_matrix[n_line]
    new_matrix[n_line] = line_to_update[:n_entry] + "0"*square_size + line_to_update[n_entry+square_size:]
  return new_matrix
      
def print_matrix(matrix):
  for line in matrix:
    for step in line:
      print(step, end=" ")
    print()
  print()

def hash_matrix(matrix):
  return hash(tuple(matrix))

memoization_table = {}

matrix_height = int(input())
matrix_width = int(input())

#build matrix
matrix = []
for i in range(matrix_height):
  line_size = int(input())
  if not line_size:
    continue  

  line = "1"*line_size + "0"*(matrix_width-line_size)
  matrix.append(line)

s_time = time.time()
print(solution(matrix) if len(matrix) else 0)
print(f"Time: {round(time.time()-s_time, 3)} seconds")