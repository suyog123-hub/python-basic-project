n = int(input("Enter the number of disks: "))

if n == 0:
    print("Invalid choice. Enter a number greater than 0.")
elif n == 1:
    print("The total number of steps is 1")
else:
    s = (2 ** n) - 1
    print("The total number of steps to move the disks is", s)