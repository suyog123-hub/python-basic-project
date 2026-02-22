import random
user=input("enter your choice rock paper or scissor").upper()
computer=random.choice(['R','P','S'])
print(user)
print(computer)
if user== 'S' and computer =="p" or user== 'P' and computer =="R" or user== 'R' and computer =="S":
    print("you win")

elif (user== 'S' and computer =="S") or (user== 'P' and computer =="P")or (user== 'R' and computer =="R"):
    print("its draw ")
else:
    print('you lose')