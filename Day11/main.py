def part1(seats):
  count = 0
  while True:
    seats, changed = applySeatingRules(seats, 4, countAdjacentSeats)
    print(count, changed)
    count += 1
    if changed == 0:
      break

  return countOccupiedSeats(seats)

def part2(seats):
  count = 0
  while True:
    seats, changed = applySeatingRules(seats, 5, countAdjacentSeatsPart2)
    print(count, changed)
    count += 1
    if changed == 0:
      break

  return countOccupiedSeats(seats)

def countOccupiedSeats(seats):
  count = 0
  for y in range(len(seats)):
    count += seats[y].count('#')
  return count

def applySeatingRules(seats, tolerance, countStrategy):
  changed = 0
  newSeats = deepcopy(seats)

  for y in range(len(seats)):
    for x in range(len(seats[y])):
      seat = seats[y][x]
      if seat == '.':
        continue
      
      adjacentSeats = countStrategy(seats, y, x)
      
      if seat == 'L':
        if adjacentSeats == 0:
          newSeats[y][x] = '#'
          changed += 1
      
      elif seat == '#':
        if adjacentSeats >= tolerance:
          newSeats[y][x] = 'L'
          changed += 1

  return newSeats, changed

def countAdjacentSeats(seats, y, x):
  count = 0
  
  # Up
  if y-1 >= 0 and seats[y-1][x] == '#':
    count += 1

  # Down
  if y+1 < len(seats) and seats[y+1][x] == '#':
    count += 1

  # Left
  if x-1 >= 0 and seats[y][x-1] == '#':
    count += 1

  # Right
  if x+1 < len(seats[y]) and seats[y][x+1] == '#':
    count += 1

  # Diagonal up-right
  if y-1 >= 0 and x+1 < len(seats[y]) and seats[y-1][x+1] == '#':
    count += 1

  # Diagonal up-left
  if y-1 >= 0 and x-1 >= 0 and seats[y-1][x-1] == '#':
    count += 1

  # Diagonal down-right
  if y+1 < len(seats) and x+1 < len(seats[y]) and seats[y+1][x+1] == '#':
    count += 1

  # Diagonal down-left
  if y+1 < len(seats) and x-1 >= 0 and seats[y+1][x-1] == '#':
    count += 1
  
  return count


def countAdjacentSeatsPart2(seats, y, x):
  n = 1000000
  count = 0
  
  # Up
  for i in range(1, n):
    yy = y-i
    if yy < 0:
      break
    seat = seats[yy][x]
    if seat == '#':
      count += 1
    if seat != '.':
      break

  # Down
  for i in range(1, n):
    yy = y+i
    if yy >= len(seats):
      break
    seat = seats[yy][x]
    if seat == '#':
      count += 1
    if seat != '.':
      break

  # Left
  for i in range(1, n):
    xx = x-i
    if xx < 0:
      break
    seat = seats[y][xx]
    if seat == '#':
      count += 1
    if seat != '.':
      break

  # Right
  for i in range(1, n):
    xx = x+i
    if xx >= len(seats[y]):
      break
    seat = seats[y][xx]
    if seat == '#':
      count += 1
    if seat != '.':
      break

  # up-right
  for i in range(1, n):
    yy = y-i
    if yy < 0:
      break
    xx = x+i
    if xx >= len(seats[y]):
      break
    seat = seats[yy][xx]
    if seat == '#':
      count += 1
    if seat != '.':
      break

  # up-left
  for i in range(1, n):
    yy = y-i
    if yy < 0:
      break
    xx = x-i
    if xx < 0:
      break
    seat = seats[yy][xx]
    if seat == '#':
      count += 1
    if seat != '.':
      break

  # down-right
  for i in range(1, n):
    yy = y+i
    if yy >= len(seats):
      break
    xx = x+i
    if xx >= len(seats[y]):
      break
    seat = seats[yy][xx]
    if seat == '#':
      count += 1
    if seat != '.':
      break

  # down-left
  for i in range(1, n):
    yy = y+i
    if yy >= len(seats):
      break
    xx = x-i
    if xx < 0:
      break
    seat = seats[yy][xx]
    if seat == '#':
      count += 1
    if seat != '.':
      break
  
  return count


with open('input.txt', "r") as input_file:
  seats = [list(line.strip()) for line in input_file.readlines()]
  print('part 1: ', part1(seats))
  print('part 2: ', part2(seats))