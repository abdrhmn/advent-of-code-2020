def part1(data):
  data = [int(line) for line in data]
  data.append(max(data)+3)
  data.sort()
  count1 = 0
  count3 = 0

  previous = 0
  for number in data:
    diff = number - previous
    if diff == 1:
      count1 += 1
    elif diff == 3:
      count3 += 1

    previous = number

  return count1 * count3

def part2(data):
  data = [0] + sorted([int(line) for line in data])

  paths = [1] + [0] * (len(data) - 1)
  for i, adapter in enumerate(data):
      for j in range(i - 3, i):
          if(adapter - data[j] <= 3):
              paths[i] += paths[j]
  
  return paths[-1]

with open('input.txt', "r") as input_file:
  data = input_file.readlines()
  print('part 1: ', part1(data))
  print('part 2: ', part2(data))