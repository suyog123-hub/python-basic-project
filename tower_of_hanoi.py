n=int(input("enter the number of disk"))
if n==1:
    print("the total number of step is 1")
elif n==0:
    print("invalid choice put the number greater than 0")
    exit()
else:
    s=((n**2)-1)
    print("the total number of step to bring the disk to destination is",s)