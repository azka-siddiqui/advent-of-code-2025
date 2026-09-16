with open("input.txt") as f:
    lines = f.readlines()

def find_largest_digit(n):
    for d in range(9, 0, -1):
        if (i := n.find(str(d))) != -1:
            return (i, str(d))

def part1():
    total_joltage = 0

    for bank in lines:
        bank = bank.strip()
        (index, digit1) = find_largest_digit(bank[:-1])
        (_, digit2) = find_largest_digit(bank[index + 1:])
        total_joltage += int(digit1 + digit2)
    
    return total_joltage

def part2():
    total_joltage = 0

    for bank in lines:
        bank = bank.strip()
        digits = []
        for i in range(11, 0, -1):
            (index, digit) = find_largest_digit(bank[:-i])
            bank = bank[index + 1:]
            digits.append(digit)
        digits.append(find_largest_digit(bank)[1])
        total_joltage += int("".join(digits))
    
    return total_joltage

print(part1())
print(part2())
