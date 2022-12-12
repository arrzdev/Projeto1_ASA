def solution(matrix):
  if not len(matrix):
    return 1

  line = matrix[0]
  #skip empty** lines
  if line.count(1) <= 1:
    return solution(matrix[1:])

  matrix_hash = hash_matrix(matrix)
  memoization_result = memoization_table.get(matrix_hash)
  if memoization_result:
    return memoization_result

  for n_entry in range(len(line)):
    #skip empty entries
    if not line[n_entry]:
      continue

    #get the max square size
    segment_size = 0
    segment_index = n_entry
    while segment_index < len(line) and line[segment_index] == 1:
      segment_size += 1
      segment_index += 1

    #calc the max square size that can be removed at position n_entry
    square_size = min(segment_size, len(matrix))

    ways_of_tilling = 0
    for n_size in range(1, square_size+1):
      new_matrix = remove_square(matrix, n_size, n_entry)
      ways_of_tilling += solution(new_matrix)
    
    memoization_table[matrix_hash] = ways_of_tilling
    return ways_of_tilling

def remove_square(matrix, square_size, n_entry):
  new_matrix = []

  #remove the square
  for matrix_line in range(len(matrix)):
    if matrix_line < square_size:
      new_line = matrix[matrix_line][:n_entry] + [0]*square_size + matrix[matrix_line][n_entry+square_size:]
    else:
      new_line = [*matrix[matrix_line]]
    new_matrix.append(new_line)

  return new_matrix
      
def print_matrix(matrix):
  for line in matrix:
    for step in line:
      print(step, end=" ")
    print()
  print()

def hash_matrix(matrix):
  matrix_tuple = tuple(tuple(row) for row in matrix)
  return hash(matrix_tuple)

memoization_table = {}

matrix_height = int(input())
matrix_width = int(input())

#build matrix
matrix = []
for _ in range(matrix_height):
  line_size = int(input())
  line = [1 if j < line_size else 0 for j in range(matrix_width)] 
  matrix.append(line)

print(solution(matrix))