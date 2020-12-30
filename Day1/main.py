def part1(input):
  for x in input:
    for y in input:
      r = x+y
      if r == 2020:
        return x * y

def part2(input):
  for x in input:
    for y in input:
      for z in input:
        r = x + y + z
        if r == 2020:
          return x * y * z


with open("input.txt", "r") as input_file:
  input = [int(x) for x in input_file.readlines()]
  print('part 1: ', part1(input))
  print('part 2: ', part2(input))
