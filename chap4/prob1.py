import random

mood = random.randrange(3)

print("I sense your energy. Your true emotions are coming across my screen.")
print("You are. . .")

if mood == 0 :
 print("\n\t\t----------------------")
 print("\n\t\tl                    l")
 print("\n\t\tl   0           0    l")
 print("\n\t\tl                    l")
 print("\n\t\tl                    l")
 print("\n\t\tl       <            l")
 print("\n\t\tl    -         -     l")
 print("\n\t\tl     -      -       l")
 print("\n\t\tl       -  -         l")
 print("\n\t\tl        -           l")
 print("\n\t\tl                    l")
 print("\n\t\t----------------------")

elif mood == 1 :
 print("\n\t\t----------------------")
 print("\n\t\tl                    l")
 print("\n\t\tl   0           0    l")
 print("\n\t\tl                    l")
 print("\n\t\tl                    l")
 print("\n\t\tl       <            l")
 print("\n\t\tl                    l")
 print("\n\t\tl                    l")
 print("\n\t\tl    ----------      l")
 print("\n\t\tl                    l")
 print("\n\t\tl                    l")
 print("\n\t\t----------------------")

elif mood == 2 :
 print("\n\t\t----------------------")
 print("\n\t\tl                    l")
 print("\n\t\tl   0           0    l")
 print("\n\t\tl                    l")
 print("\n\t\tl                    l")
 print("\n\t\tl       <            l")
 print("\n\t\tl                    l")
 print("\n\t\tl                    l")
 print("\n\t\tl       ------       l")
 print("\n\t\tl    ---       ---   l")
 print("\n\t\tl                    l")
 print("\n\t\t----------------------")

else :
 print("\nIllegal mood value!")

print("\n...today.")
