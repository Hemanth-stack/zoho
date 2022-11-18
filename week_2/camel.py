s = input("camelCase: ")
new_s = ""
for i in s:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        new_s += "_"
        new_s += i.lower()
    else:
        new_s += i
print(new_s)
