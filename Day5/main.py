def getBoardingPassIds(data):
  return [getBoardingPassId(line) for line in data]

def part2(ids): 
  for id in ids:
    if id+1 not in ids and id+2 in ids:
      return id+1

def getBoardingPassId(bp):
  return getBoardingPassRow(bp) * 8 + getBoardingPassColumn(bp)

def getBoardingPassRow(bp):
  rows = bp[:7]
  return int(decodeRows(rows), 2)

def getBoardingPassColumn(bp):
  columns = bp[7:]
  return int(decodeColumns(columns), 2)

def decodeRows(rows):
  return rows.replace('F', '0').replace('B', '1')

def decodeColumns(columns):
  return columns.replace('L', '0').replace('R', '1')


with open('input.txt', "r") as input_file:
  data = input_file.readlines()
  ids = getBoardingPassIds(data)
  print('part 1: ', max(ids))
  print('part 2: ', part2(ids))