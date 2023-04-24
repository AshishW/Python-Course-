# Error Handling
try:
    age = int(input('enter your age: '))
    print(age)
except:
    print("please enter a number")

# but there is a problem with the above code that if the age is not valid, it says 'please enter a number' but it does not asks us to enter age again
# So, to fix this we can use a while loop

while True:
    try:
        age = int(input('enter your age: '))
        print(age)
    except:  # except block is executed if there is exception/error in the try block
        print('please enter valid age')
    else:  # else runs if there is no exception
        print('thank you!')
        break
# specific exception
while True:
    try:
        age = int(input('enter your age: '))
        print(age)
    except ValueError as err:  # except block is executed if there is exception/error in the try block
        print(f'please enter valid age {err}')
    else:  # else runs if there is no exception
        print('thank you!')
        break
    finally:
        print("ohh, finally it's all done! 😅")

# the most common cases where we have to do error handling is when we accept an input from a user
# and when I say input, it's not only the input() function. I mean by functions accepting arguments, classes accepting input like method calls or trying to change attributes
