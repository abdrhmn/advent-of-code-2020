def part1(data):
  vaidCount = 0
  for line in data:
    lineParts = line.split(':')
    policy = lineParts[0].strip().split(' ')
    password = lineParts[1].strip()

    min = int(policy[0].split('-')[0])
    max = int(policy[0].split('-')[1])
    letter = policy[1]

    if min <= password.count(letter) <= max:
      vaidCount += 1

  return vaidCount

def part2(data):
  vaidCount = 0
  for line in data:
    lineParts = line.split(':')
    policy = lineParts[0].strip().split(' ')
    password = lineParts[1].strip()

    firstIndex = int(policy[0].split('-')[0])-1
    secondIndex = int(policy[0].split('-')[1])-1
    letter = policy[1]

    firstIndexValid = password[firstIndex] == letter
    secondIndexValid = password[secondIndex] == letter
 
    if sum([firstIndexValid, secondIndexValid]) == 1:
      vaidCount += 1

  return vaidCount 


with open("input.txt", "r") as input_file:
  input = input_file.readlines()
  print('part1: ', part1(input))
  print('part2: ', part2(input))