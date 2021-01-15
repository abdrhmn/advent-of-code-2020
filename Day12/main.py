def part1(actions):
  x = 0
  y = 0
  direction = 90

  for action in actions:
    x, y, direction = applyAction(action, x, y, direction)    
  
  return abs(x) + abs(y)

def applyAction(action, x, y, direction):
  command = action[:1]
  value = int(action[1:])
  
  if command == 'N':
    y += value
  elif command == 'S':
    y -= value
  elif command == 'E':
    x += value
  elif command == 'W':
    x -= value
  
  elif command == 'R':
    direction = (direction + value) % 360
  elif command == 'L':
    direction = (direction - value) % 360

  elif command == 'F':
    if direction == 0:
      y += value
    elif direction == 180:
      y -= value
    elif direction == 90:
     x += value
    elif direction == 270:
      x -= value

  return x, y, direction

def part2(actions):
  wx = 10
  wy = 1
  x = 0
  y = 0

  for action in actions:
    wx, wy, x, y = applyAction2(action, wx, wy, x, y)

  return abs(x) + abs(y)

def applyAction2(action, wx, wy, x, y):
  command = action[:1]
  value = int(action[1:])
  
  if command == 'N':
    wy += value
  elif command == 'S':
    wy -= value
  elif command == 'E':
    wx += value
  elif command == 'W':
    wx -= value

  elif command == 'R':
    if value == 90:                                                                    
      wxCopy = wx
      wx = wy
      wy = wxCopy * -1
    elif value == 180:
      wx *= -1
      wy *= -1
    elif value == 270:
      wyCopy = wy
      wy = wx
      wx = wyCopy * -1

  elif command == 'L':
    if value == 90:
      wxCopy = wx
      wx = wy * -1
      wy = wxCopy
    elif value == 180:
      wx *= -1
      wy *= -1
    elif value == 270:
      wyCopy = wy
      wy = wx * -1
      wx = wyCopy

  elif command == 'F':
    x += wx * value
    y += wy * value

  return wx, wy, x, y


with open('input.txt', "r") as input_file:
  actions = [line.strip() for line in input_file.readlines()]
  print('part 1: ', part1(actions))
  print('part 2: ', part2(actions))


