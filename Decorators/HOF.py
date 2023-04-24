#Higher Order Function HOC
def func1():
    return 'hello'

def greet(func1): #HOC eg 1
    func1()

def greet2(): #HOC eg. 2
    def func():
        return 5
    return func

#Higher Order Function is any function that either accepts a function as a parameter or returns a function
#map, reduce, filter are examples of higher order function