import re

string = 'search inside of this text please'

print(re.search('this', string).group())