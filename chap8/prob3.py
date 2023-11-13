text_file = open("write_2.txt" , "w")

print("Input your string  ...")
    
while True:
    line = input(">> ")
    text_file.write(line+"\n")
    if(line == 'Q'):
        break

text_file.close()


print("Write process has been finished")
print("\n\n\nYour inputs are below...")



text_file = open("write_2.txt","r")

for line in text_file:
    print(line,end ='')

text_file.close()

    
