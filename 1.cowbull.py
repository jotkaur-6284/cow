import random
bull=0
cow=0
g=1
nbull=0
num=str(random.randint(1000,9000))
print(num)
guess=int(input("enter number how many time you want to try="))
j=0
while j<guess:
    g=list(input("enter your guess"))
    for i,c in enumerate(num):
        if g[i]==num[i]:
            bull+=1
            nbull+=1
        else:
            for s,z in enumerate(g):
                if num[i]==g[s]:
                    cow+=1
    print("bull",bull,"cow",cow)                    
    if bull==4:
        print("waoo your guess is right")
        break
    # else:
    #     print("wrong")
    bull=0
    cow=0
    j+=1
if nbull==4:
    print("waoo your guess is right")
else:    
    print("sory! your guess is wrong")
    print(num,"is the number")