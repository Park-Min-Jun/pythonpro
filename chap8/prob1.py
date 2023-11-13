text_file = open("read_it.txt" , "r")

print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print()
text_file = open("read_it.txt" , "r")
whole_thing = text_file.read()

print(whole_thing)
text_file.close()

text_file = open("read_it.txt" , "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print()
text_file = open("read_it.txt" , "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

text_file = open("read_it.txt" , "r")
lines = text_file.readlines()
print(lines)
text_file.close()

text_file = open("read_it.txt" , "r")
for line in text_file:
    print(line)
text_file.close()
