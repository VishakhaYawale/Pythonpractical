f = open("first.txt", "wt")
f.write("This is a line")

with open('first.txt', 'a') as f:
    f.write('Hello')