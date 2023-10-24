bomb = {"404": "clueless.",
        "Uninstalled": "being fired. Especially popular during the dot-bomb era."}
       

while True:
    print("\n\t Geek Translator")
    print("\n\t 0 - Quit")
    print("\t 1 - Look up a Geek Term")
    print("\t 2 - Add a Geek Term")
    print("\t 3 - Redefine a Geek Term")
    print("\t 4 - Delete a Geek Term")
    
    num = int(input("Choice: "))
    print()
    
    if num == 0:
        input("Press the enter to exit.")
        break;

    elif num == 1:
        key = input("What term do you want me to translate?: ")
        if key in bomb:
            mean  = bomb[key]
            print("\n%s means %s"%(key ,mean))

    elif num == 2:
        key = input("What term do you want me to add?: ")
        if key not in bomb:
            mean = input("What's the definition?: ")
            bomb[key] = mean
            print("\n%s has been added." %(key))

    elif num == 3:
        key = input("What term do you want me to redefine?: ")
        if key in bomb:
            mean = input("What's the new definition?: ")
            bomb[key] = mean
            print("\n %s has been redefined" %(key))

    elif num == 4:
        key = input("What term do you want to delete?: ")
        if key in bomb:
            del bomb[key]
            print("%s has deleted"%(key),end = '')
