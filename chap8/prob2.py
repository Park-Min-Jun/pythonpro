print("Creating a text file with the write() method\n")

text_file = open("write_it.txt" , "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("Thatmakes this line 3\n")
text_file.close()

text_file = open("write_it.txt" , "r")
for line in text_file:
    print(line)
text_file.close()

print("Creating a text file with the writelines() method\n")
text_file = open("write_it.txt" , "w")
lines = ["Line 1\n", "This is line 2\n" , "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

text_file = open("write_it.txt" , "r")
for line in text_file:
    print(line)
text_file.close()
