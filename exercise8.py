import sys

dict = {}

with open (sys.argv[1]) as file:
    for line in file:
        x = str(line.splitlines()).replace("['","").replace("']","")
        name = x.split(":")[0]
        uni = x.split(":")[1]
        dict[name] = uni
print(dict)

for names in sys.argv[2].split(","):
    try:
        print("Name:",names,",","University:",dict[names])
    except KeyError:
        print( f"No record of {names} was found!")
