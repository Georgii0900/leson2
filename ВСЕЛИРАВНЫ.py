first = int(input())
second = int(input())
third = int(input())
if first == second == third:
    print(3)
elif first == second != third or first == third != second or third == second != first:
    print(2)
else :
    if first != second != third:
        print(0)
