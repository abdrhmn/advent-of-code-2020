import re

def cleanPassportData(data):
  passports = []
  passport = ''
  
  for line in data:
    line = line.strip()
    if not line:
      passports.append(passport.strip())
      passport = ''
      continue
  
    passport += ' ' + line
  passports.append(passport.strip())
  
  return passports

def part1(passports):
  validPassportsCount = 0
  for passport in passports:
    if passportHasAllRequiredFields(passport):
      validPassportsCount += 1

  return validPassportsCount

def part2(passports):
  validPassportsCount = 0
  for passport in passports:
    # passport = passport.strip()
    if passportHasAllRequiredFields(passport) and isPassportFieldsValid(passport):
      validPassportsCount += 1

  return validPassportsCount

def passportHasAllRequiredFields(passport):
  requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  attributes = passport.split(' ')
  passportFields = []
  for attribute in attributes:
    passportFields.append(attribute.split(':')[0])
  
  # validate required fields
  if not all(field in passportFields for field in requiredFields):
    return False
  
  return True

def isPassportFieldsValid(passport):
  attributes = passport.split(' ')
  for attribute in attributes:
    if not isAttributeValid(attribute):
      return False

  return True

def isAttributeValid(attribute):
  key = attribute.split(':')[0]
  value = attribute.split(':')[1]

  if key == 'byr':
    value = int(value)
    if not (value >= 1920 and value <= 2002):
      return False

  elif key == 'iyr':
    value = int(value)
    if not (value >= 2010 and value <= 2020):
      return False
  
  elif key == 'eyr':
    value = int(value)
    if not (value >= 2020 and value <= 2030):
      return False

  elif key == 'hgt':
    unit = value[-2:]
    if unit == 'cm':
      value = int(value[:-2])
      if not (value >= 150 and value <= 193):
        return False

    elif unit == 'in':
      value = int(value[:-2])
      if not (value >= 59 and value <= 76):
        return False
    
    else:
      return False

  elif key == 'hcl':
    if not value[0] == '#':
      return False
    
    value = value[1:]
    if not len(value) == 6:
      return False
    if not re.match('^[a-f0-9]+$', value):
      return False

  elif key == 'ecl':
    if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
      return False
  
  elif key == 'pid':
    if not len(value) == 9:
      return False
    if not re.match('^[0-9]+$', value):
      return False

  return True


with open('Day4/input.txt', "r") as input_file:
  data = cleanPassportData(input_file.readlines())
  print('part 1: ', part1(data))
  print('part 2: ', part2(data))