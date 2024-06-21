bet=int(input("enter a number which falls in 0-36 inclusive:"))
if bet == 0:
  print("green")
if bet > 0 and bet <=10:
  if bet % 2==0:
    print("black")
  else:
    print("red")
if bet > 10 and bet <=18:
  if bet % 2 ==0:
    print("red")
  else:
    print("black")
if bet > 18 and bet <=28:
  if bet % 2 ==0:
    print("black")
  else:
    print("red")
if bet >28  and bet <= 36:
  if bet % 2==0:
    print("red")
  else:
    print("black")

if bet > 36:
  print("The bet will not play!")
  bet=int(input(" please pick a number that falls in the range: "))
