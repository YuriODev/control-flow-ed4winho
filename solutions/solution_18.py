# Predefined outcomes as constants

greeting = input("Do you remember the person's name? (yes/no): ")
name = input("Do you know their name? (yes/no): ")
ex = input("Are they an ex? (yes/no): ")
unusual = input("Are you in an unusual situation? (yes/no): ")
print(decide(greeting, name, ex, unusual))
def decide(greeting, name, ex, unusual):
  if greeting.lower() == 'yes':
      if ex.lower() == 'yes':
          return "Keep walking"
      else:
          if unusual.lower() == 'yes':
              return "Don't say hi"
          else:
              return "Say hi"
  elif greeting.lower() == 'no':
      if ex.lower() == 'yes':
          return "Keep walking"
      else:
          if unusual.lower() == 'yes':
              return "Keep walking"
          else:
              return "Don't say hi"
