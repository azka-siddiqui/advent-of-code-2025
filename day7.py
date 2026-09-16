with open("input.txt") as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]

def part1():
    times_split = 0
    lines_part1 = [line.copy() for line in lines]
    s_index = lines_part1[0].index("S")
    lines_part1[1][s_index] = "|"

    for i in range(2, len(lines_part1)):
        for j in range(len(lines_part1[0])):
            if lines_part1[i - 1][j] == "|":
                if lines_part1[i][j] == ".":
                    lines_part1[i][j] = "|"
            elif lines_part1[i - 1][j] == "^":
                if lines_part1[i - 2][j] == "|":
                    times_split += 1
                    lines_part1[i][j - 1] = "|"
                    lines_part1[i][j + 1] = "|"
    
    return times_split

memory = {i: {} for i in range(len(lines))}

def travel(i, j, count):
    if i >= len(lines):
        return 1
    elif lines[i][j] == "^":
        if j in memory[i]:
            return memory[i][j]
        memory[i][j] = travel(i + 1, j - 1, count) + travel(i + 1, j + 1, count)
        return memory[i][j]
    else:
        if j in memory[i]:
            return memory[i][j]
        memory[i][j] = travel(i + 1, j, count)
        return memory[i][j]

def part2():
    s_index = lines[0].index("S")
    return travel(1, s_index, 0)

print(part1())
print(part2())
