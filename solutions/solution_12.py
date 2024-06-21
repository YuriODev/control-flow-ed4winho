def replace_digits_with_char(number, char):
  number_str = str(number)
  replaced_str = ""

  for digit in number_str:
      if digit.isdigit():
          replaced_str += char
      else:
          replaced_str += digit

  replaced_number = int(replaced_str)
  return replaced_number

number = 12345
char_to_replace = '*'

new_number = replace_digits_with_char(number, char_to_replace)
print(new_number)
