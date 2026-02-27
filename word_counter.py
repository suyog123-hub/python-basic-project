user=input("enter the word or the paragraph ")
repeat={}
for i in user.split():
    if i  in repeat:
        repeat[i]+=1
    else:
        repeat[i]=1

for word ,count in repeat.items():
    print(f'{word}:{count}')