with open("input.txt") as f:
    lines = f.readlines()

def part1():
    numbers = [[int(n.strip())] for n in lines[0].split()]
    for line in lines[1:-1]:
        new_numbers = [int(n.strip()) for n in line.split()]
        for i in range(len(numbers)):
            numbers[i].append(new_numbers[i])
    operations = [o.strip() for o in lines[-1].split()]

    total = 0

    for i in range(len(operations)):
        if operations[i] == '+':
            total += sum(numbers[i])
        elif operations[i] == '*':
            product = 1
            for n in numbers[i]:
                product *= n
            total += product

    return total

def part2():
    numbers = [line[:-1] for line in lines[:-1]]
    operations = lines[-1]

    total = 0

    index = len(operations) - 1
    while index >= 0:
        index -= 1
        problem_numbers = []

        while operations[index] == ' ':
            problem_numbers.append([])
            for i in range(len(numbers)):
                problem_numbers[-1].append(numbers[i][index])
            index -= 1

        problem_numbers.append([])
        for i in range(len(numbers)):
            problem_numbers[-1].append(numbers[i][index])
                
        problem_numbers = [int("".join(n)) for n in problem_numbers]
        if operations[index] == '+':
            total += sum(problem_numbers)
        elif operations[index] == '*':
            product = 1
            for n in problem_numbers:
                product *= int(n)
            total += product
        
        index -= 1

    return total

print(part1())
print(part2())
