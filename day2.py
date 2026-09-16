with open("input.txt") as f:
    id_ranges = f.readline().split(",")

def is_invalid_part1(id_str):
    return str(id_str)[:len(str(id_str)) // 2] == str(id_str)[len(str(id_str)) // 2:]

def is_invalid_part2(id_str):
    for i in range(1, (len(id_str) // 2) + 1):
        if (len(id_str) % i) == 0:
            for j in range(1, (len(id_str) // i)):
                if id_str[:i] != id_str[i * j:i * (j + 1)]:
                    break
                elif j == (len(id_str) // i) - 1:
                    return True
    return False

def day2():
    invalid_sum_part1 = 0
    invalid_sum_part2 = 0

    for id_range in id_ranges:
        start, end = id_range.split("-")
        for i in range(int(start), int(end) + 1):
            if is_invalid_part1(str(i)):
                invalid_sum_part1 += i
            if is_invalid_part2(str(i)):
                invalid_sum_part2 += i
    
    return (invalid_sum_part1, invalid_sum_part2)

print(day2())
