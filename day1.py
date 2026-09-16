with open("input.txt") as f:
    lines = f.readlines()

def part1():
    dial = 50
    password = 0

    for line in lines:
        direction, value = line[0], int(line[1:])

        if direction == "L":
            dial -= value
        elif direction == "R":
            dial += value
        
        dial %= 100
        if dial == 0:
            password += 1
    
    return password

def part2():
    dial = 50
    password = 0

    for line in lines:
        direction, value = line[0], int(line[1:])

        if direction == "L":
            for _ in range(value):
                dial -= 1
                if dial == -1:
                    dial = 99
                if dial == 0:
                    password += 1
        elif direction == "R":
            for _ in range(value):
                dial += 1
                if dial == 100:
                    dial = 0
                if dial == 0:
                    password += 1
    
    return password

print(part1())
print(part2())
