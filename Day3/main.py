def countTrees(data, rightStep, downStep):
  treesCount = 0
  n = 31
  rightPosition = 0
  downPosition = 0
    
  while downPosition < len(data):
    line = data[downPosition]

    positionInMap = line[rightPosition%n]
    if positionInMap == '#':
      treesCount += 1

    rightPosition += rightStep
    downPosition += downStep

  return treesCount

def part2(data):
  return countTrees(data, 1, 1) * countTrees(data, 3, 1) * countTrees(data, 5, 1) * countTrees(data, 7, 1) * countTrees(data, 1, 2)


with open("input.txt", "r") as input_file:
  input = input_file.readlines()
  print('part 1: ', countTrees(input, 3, 1))
  print('part 2: ', part2(input))