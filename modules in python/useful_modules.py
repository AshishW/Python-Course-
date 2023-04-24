from collections import Counter, defaultdict, OrderedDict

#Counter  is useful if we have duplicate emails, users etc

li = [1,2,3,4,5]
print(Counter(li)) # Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})

sentence = 'hey! how are you'
print(Counter(sentence)) 
# Counter({' ': 3, 'h': 2, 'e': 2, 'y': 2, 'o': 2, '!': 1, 'w': 1, 'a': 1, 'r': 1, 'u': 1})

# So Counter just tells us, how many times each things occurs and gives us a hashtable/dictionary


#DEFAULTDICT

dictionary = {
    'a': 1,
    'b': 2
}

# now to access any key of the dictionary, we can use the below syntax
dictionary['a']

# but what if we try to access key that doesn't exist in the object/dictionary?
# If we try doing something like 'dictionary['c']', it will throw an error
# So can we have a default value if we try to access something that doesn't exist in the dictionary?
# Yes! We can use the default dictionary in-built module

dictionary2 = defaultdict( lambda:'key not found',{ # we are using lambda function to set the default value
    'a': 1,
    'b': 2
})

# the first thing that defaultdict takes is a callable where we set the default value
# the second argument is the object/dictionary

print(dictionary2['c']) # this will print 'key not found' (default value) instead of throwing error

#ORDERED DICT

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
# d = {
#     'a': 1,
#     'd': 3
# }

# d1 = {
#     'd':3,
#     'a': 1
# }

print(d == d2)


# DATE TIME

import datetime

print(datetime.date.today())
print(datetime.time(3,45,9))

# array

from array import array 
# arrays are more performant than lists. So we can use it if we don't want to use generators to optimize the performance of the code.

arr = array('i', [1,2,3])
print(arr[0])