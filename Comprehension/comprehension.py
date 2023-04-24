# comprehension for list


my_list = [char for char in 'hello']
print(my_list)

list2 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(list2)  # only even no.

# comprehension exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# for value in some_list:
#     if some_list.count(value) > 1 and value not in duplicate:
#         duplicate.append(value)

duplicate = list({v for v in some_list if some_list.count(v) > 1})  # v -> value
print(duplicate)
