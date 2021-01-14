info = ["A", "22", "B", "25", "C", "34"]
age = []

for i in info:
    try:
        int(i)
        age.append(i)
    except:
        pass
print("{}".format(age))

