import random

herohp = random.randrange(50,100)
monsterhp = random.randrange(50,100)

value = random.randrange(-10,20)
value2 = random.randrange(-10,20)

print("hero HP : ",herohp,",","monster HP : ", monsterhp)

 while(herohp >= 0 or monsterhp >= 0):

    if(value <= 0):
        attack = ('fail')
    else :
        attack = ('success')
        herohp = herohp - value

    if(value2 <= 0):
        attack2 = ('fail')
    else : 
        attack2 = ('success')
print("hero(HP : " , herohp , " attack : " , value , ")" , attack)
