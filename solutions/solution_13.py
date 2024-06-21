def check_unique_digits(n):
  digits = [int(d) for d in str(n)]
  return len(set(digits)) == len(digits)

number = int(input("Enter a four-digit number: "))
result = check_unique_digits(number)
print(result)
