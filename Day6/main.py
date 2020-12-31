def part1(data):
  group = ''
  groups = []

  for line in data:
    line = line.strip()
    if not line:
      groups.append(group)
      group = ''
      continue
  
    group += line
  
  groups.append(group)

  sum = 0
  for group in groups:
    sum += len("".join(set(group)))

  return sum

def part2(data):
  group = ''
  groups = []

  for line in data:
    line = line.strip()
    if not line:
      groups.append(group)
      group = ''
      continue
  
    if group == '':
      group += line
    else:
      group += ':' + line
  groups.append(group)

  sum = 0
  for group in groups:
    intersect = set(group.split(':')[0])
    for person in group.split(':'):
      intersect = intersect & set(person)
    sum += len(intersect)

  return sum

with open('input.txt', "r") as input_file:
  data = input_file.readlines()
  print('part 1: ', part1(data))
  print('part 2: ', part2(data))