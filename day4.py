with open("input.txt") as f:
    lines = f.readlines()
    grid = [list(line.strip()) for line in lines]

def count_adjacent_rolls(i, j):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for y, x in directions:
        a, b = i + y, j + x
        if (0 <= a < len(grid)) and (0 <= b < len(grid[0])):
            if grid[a][b] == "@":
                count += 1

    return count

def part1():
    accessible_rolls = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                if count_adjacent_rolls(i, j) < 4:
                    accessible_rolls += 1
    
    return accessible_rolls

def part2():
    prev_removable_rolls = -1
    removable_rolls = 0

    while (removable_rolls != prev_removable_rolls):
        prev_removable_rolls = removable_rolls
        rolls_to_remove = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    if count_adjacent_rolls(i, j) < 4:
                        removable_rolls += 1
                        rolls_to_remove.append((i, j))
        
        for c, d in rolls_to_remove:
            grid[c][d] = "."

    return removable_rolls

print(part1())
print(part2())
