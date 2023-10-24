inventory = ["sword",
             "armor",
             "shield",
             "healing potion"]

print ("Your items:\t")

for item in inventory:
 print (item)

input ("\nPress the enter key to continue.")
print ("You have ", len(inventory), "items in your possession.")
input ("\nPress the enter key to continue.")

if "healing potion" in inventory:
    print ("You will live to fight another day.")

index = int(input("\nEnter an index number for an item in inventory:\t"))

print ("At index ", index, "is", inventory[(index)])
begin = int(input("\nEnter an index number to begin a slice:\t"))
end = int(input("Enter an index number to end the slice:\t"))

print ("inventory[", begin, ":", end, "] \t\t", end = "")
print (inventory[start:end])
input ("\nPress Enter to continue.")

chest = ["gold", "gems"]

print ("You find a chest. It contains:\t")
print (chest)
print ("You add the contents of the chest to your inventory.")

inventory += chest
print("Your inventory is now :")
print(inventory)
input ("\nPress Enter key to continue.")
print("You trade your sword for a crossbow.")
print("Your inventory is now:")

inventory[0]= "crossbow"
print(inventory)
input("\npress the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]

print(inventory)
input("\nPress the enter key to continue.")
print("In a great battle, your sheild is destroyed.")

del inventory[2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")

del inventory[:2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to exit.")
