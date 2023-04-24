# Standard Way To Read File:
# common pattern in IO is to use try except blocks

# r+ read and write
# a  to append text at end
try:
    with open('./test.txt', mode='a') as my_file:
        text = my_file.write(':)')
        print(text)

    with open('./create.txt', mode='w') as my_file:
        text = my_file.write('This is created using python')
        print(text)
except FileNotFoundError as err:
    print("file doesn't exist")
    raise err
except IOError as err: # IOError occurs when machine is not able to do any sort of IO operations
    print('IO error')
    raise err

# to have paths which are more compatible i.e. work on different machines such as mac, windows and linux,
# we can use pathlib in-built python module (https://docs.python.org/3/library/pathlib.html)