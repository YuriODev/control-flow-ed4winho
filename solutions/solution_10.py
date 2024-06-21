def is_right_angle(a, b, c):
    ab = (a[0] - b[0])**2 + (a[1] - b[1])**2
    bc = (b[0] - c[0])**2 + (b[1] - c[1])**2
    ca = (c[0] - a[0])**2 + (c[1] - a[1])**2
    sides = [ab, bc, ca]
    sides.sort()
    return sides[0] + sides[1] == sides[2]

# Input
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

if is_right_angle(a, b, c):
    print("Yes")
else:
    print("No")
