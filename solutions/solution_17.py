ticket = input("Enter a ticket number: ")
print(check_lucky(ticket))
def check_lucky(ticket):
    sum_first = sum(int(digit) for digit in ticket[:3])
    sum_last = sum(int(digit) for digit in ticket[3:])
    if sum_first == sum_last:
        return "Happy"
    else:
        return "Ordinary"
