a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
c = int(input("Enter 3rd Number:"))

if a > b and a > c:
    print("1st number is Greater")
elif b > a and b > c:
    print("2nd number is Greater")
else:
    print("3rd Number is Greater")