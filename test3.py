import re

pat = re.compile(".*[.](?!bat$exe$).*$")
m=pat.match("a.bat")

if m:
    print('true: ', m.group())

else:
    print('No match')    