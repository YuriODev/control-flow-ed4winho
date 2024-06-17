# Prompt the user to enter their age and convert it to an integer
age=int(input("input your age:"))
if age <= 1:
  print("you are a inphant:")
elif age > 1 and age<13:
  print("you are a child")
elif age >= 13 and age<20:
  print('you are a teenager')
elif age>20:
  print("you are an adult")

