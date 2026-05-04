import random
LS=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NS=["0","1","2","3","4","5","6","7","8","9"]
SS=["!","@","#","$","%","^","&","*","(",")","-","+","=","{","}","[","]",":",";","<",">",",",".","?","/"]
print("----Welcome to the Password Generator!----")
nls=int(input("How many letters do you want in your password?:"))
nns=int(input("How many numbers do you want in your password?:"))
nss=int(input("How many symbols do you want in your password?:"))
PL=[]
for i in range(nls):
    c=random.choice(LS)
    PL.append(c)
for i in range(nns):
    c=random.choice(NS)
    PL.append(c)
for i in range(nss):
    c=random.choice(SS)
    PL.append(c)
random.shuffle(PL)
password=""
for i in PL:
    password+=i
print(f"Your password is: {password}")
