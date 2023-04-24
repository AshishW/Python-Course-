# lamda expressions
# lambda param: action(param)


from functools import reduce



my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list))

# exercies lambda expression

# square
list1 = [5, 4, 3]

print(list(map(lambda i: i**2, list1)))

# list sorting: sort based on second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

b = [(1,2), (2,0)]
def fun(x):
    print(x)
    return x[1]


b. sort(key= fun)
print(b)