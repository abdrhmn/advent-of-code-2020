def findFirstInvalidNumber(data, preamble = 25):
  data = [int(line.strip()) for line in data]

  for index, number in enumerate(data):
    if index < preamble:
      continue
    
    previousNumbers = data[index-preamble:index]
    if isNumberValid(previousNumbers, number):
      continue
    
    return number

def isNumberValid(preambleNumbers, number):
  n = len(preambleNumbers)
  for i in range(n):
    for j in range(i+1, n):
      if preambleNumbers[i] + preambleNumbers[j] == number:
        return True
  
  return False


def part2(data, invalidNumber):
  contiguousNumbers = findContiguousNumbers(data, invalidNumber)

  return min(contiguousNumbers) + max(contiguousNumbers)

def findContiguousNumbers(data, invalidNumber):
  data = [int(line.strip()) for line in data]

  n = len(data)
  for i in range(n):
    contiguousNumbers = [data[i]]
    for j in range(i+1, n):
      if sum(contiguousNumbers) + data[j] == invalidNumber:
        return contiguousNumbers
      contiguousNumbers.append(data[j])

  print(':(')
  return False

with open('input.txt', "r") as input_file:
  data = input_file.readlines()
  invalidNumber = findFirstInvalidNumber(data)
  print('part 1: ', invalidNumber)
  print('part 2: ', part2(data, invalidNumber))