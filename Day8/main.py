def part1(data):
  data = [line.strip() for line in data]
  
  index = 0
  acc = 0
  excutedLines = []
  
  while True:
    if index in excutedLines:
      return acc, False

    if index >= len(data):
      return acc, True

    excutedLines.append(index)
    line = data[index]
    instruction = line.split(' ')[0]
    argument = line.split(' ')[1]

    if instruction == 'acc':
      acc += float(argument)
      index += 1

    elif instruction == 'jmp':
      index += int(argument)

    else:
      index += 1

  return acc

def part2(data):
  data = [line.strip() for line in data]
  for i in range(len(data)):
    if 'jmp' in data[i]:
      data[i] = data[i].replace('jmp', 'nop')
      acc, solved = part1(data)

      if solved:
        return acc
      else:
        data[i] = data[i].replace('nop', 'jmp')
  
  return 'FFF'
      
with open('input.txt', "r") as input_file:
  data = input_file.readlines()
  print('part 1: ', part1(data))
  print('part 2: ', part2(data))