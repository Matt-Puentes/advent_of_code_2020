numbers = []
with open("input", "r") as f:
    numbers = f.readlines()

numbers = [int(x) for x in numbers]
print(numbers)

for x in numbers:
    for y in numbers:
        if(x + y > 2020):
            continue
        for z in numbers:
            if(x + y + z == 2020):
                print(x * y * z)