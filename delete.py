import os
x = open("to_delete", "r").read().splitlines()
for y in x:
    os.remove(y)
