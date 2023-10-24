scores = []

while True:
    print("\t High Scores keeper")
    print("\t 0 - Quit")
    print("\t 1 - List Scores")
    print("\t 2 - Add a score")
    num = int(input("\nChoice: "))
   
    if num == 0:
        input("\nPress the Enter to exit.")
        break;
    elif num == 1:
        print ("\nHigh Scores")
        print ("\nNAME\tSCORE")
        for entry in scores:
            name, score = list1
            print (name,"\t",score)
        print()

    if num == 2:
        name = input("\nWhat is the player's name?: ")
        score =int(input("What score did the player's get?: "))
        print()
        list1 = (name,score)
        scores.append(entry)
        scores.sort
