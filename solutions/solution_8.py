def check_digit_in_number(num, digit):
  num_str = str(num)
  digit_str = str(digit)

  for char in num_str:
      if char == digit_str:
          return True

  return False

number = int(input("Enter a three-digit number: "))
digit = int(input("Enter a digit to check: "))

result = check_digit_in_number(number, digit)
print(result)
