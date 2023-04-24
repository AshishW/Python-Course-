my_file = open('./test.txt')

# to read the file we can use the read function

print(my_file.read())
my_file.seek(0) # resets the cursor position to starting of the file
print(my_file.read())
my_file.seek(0) # resets the cursor position to starting of the file
print(my_file.read())

print("*" * 100 + '\n')

# using readline and readlines function

my_file.seek(0)
print(my_file.readline()) # prints only one line
my_file.seek(0)
print(my_file.readlines()) # gives list having each lines as its items

my_file.close()