# decorator
# decorator super charges a function


# decorator pattern
from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        print(func)
        func(*args, **kwargs)
    return wrap_func


@my_decorator
def hello(greeting, emoji=":)"):
    print(greeting, emoji)


hello('hi')

# why do we need decorators?


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i * 5

@performance
def long_time2():
    for i in list(range(10000000)):
        i * 5

long_time()
long_time2()


# # Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#     def wrapper(*args, **kwargs):
#         if args[0]['valid']:
#             return fn(*args, **kwargs)
#         else:
#             print('user not valid') 
#     return wrapper

# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)