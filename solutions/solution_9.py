def compare_digits(num):
  num_str = str(num)

  first_digit = int(num_str[0])
  second_digit = int(num_str[1])
  last_digit = int(num_str[2])

  sum_first_last = first_digit + last_digit

  if sum_first_last > second_digit:
      print(">")
  elif sum_first_last < second_digit:
      print("<")
  else:
      print("=")

number = int(input("Enter a three-digit number: "))
compare_digits(number)
