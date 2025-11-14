s
'''
1 = snake 
2 = water
3 = gun

'''



import random
computer = random.choice([1,2,3])
yourchoice = input("enter your coice boy (s = snake) or (w = water ) or (g = gun ) - ")
userdict = {"s" : 1 , "w" : 2, "g" : 3}
reverdict = {1:"snake", 2 :"water", 3:"gun"}
usernum = userdict[yourchoice]
print(f"your choice is {reverdict[usernum]} computer coice is {reverdict[computer]}")
if(computer==usernum):
    print("its a draw ")
else:
    if(computer==1 and usernum==2):
        print("als ! you lost ")
    elif(computer==1 and usernum==3):
        print("hurray you won!")
    elif(computer==2 and usernum==3):
        print("als ! you lost ")
    elif(computer==2 and usernum==1):
        print("hurray you won!")
    elif(computer==3 and usernum==1):
        print("als ! you lost ")
    elif(computer==3 and usernum==3):
        print("hurray you won!")
    else:
        print("something is wrong bro ")
