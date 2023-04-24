# creating for loop from scratch:

def new_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


new_for([1, 2, 3])

# creating generator from scratch


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

g = MyGen(0, 10)
for i in g:
    print(i)



def fib(num):
    current = 0
    next = 1
    for i in range(num):
        # print(a)
        yield current
        temp = current
        current = next
        next = temp + next

   
for x in fib(20):
    print(x)
