import re

pattern = r'life'

string = "life of human"
print(re.match(pattern, string).group())

