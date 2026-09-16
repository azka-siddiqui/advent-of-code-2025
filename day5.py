with open("input.txt") as f:
    lines = f.readlines()
    id_ranges = [([int(x) for x in line.strip().split("-")]) for line in lines[:lines.index("\n")]]
    available_ids = [int(line.strip()) for line in lines[lines.index("\n") + 1:]]

def part1():
    count_fresh_ids = 0

    for available_id in available_ids:
        for id_range in id_ranges:
            if id_range[0] <= available_id <= id_range[1]:
                count_fresh_ids += 1
                break

    return count_fresh_ids

def part2():
    count_total_fresh_ids = 0
    id_ranges.sort(key=lambda r: r[0])
    merged_id_ranges = [id_ranges[0]]

    for id_range in id_ranges[1:]:
        if id_range[0] <= merged_id_ranges[-1][1]:
            merged_id_ranges[-1][1] = max(merged_id_ranges[-1][1], id_range[1])
        else:
            merged_id_ranges.append(id_range)
    
    for merged_id_range in merged_id_ranges:
        count_total_fresh_ids += merged_id_range[1] - merged_id_range[0] + 1
    
    return count_total_fresh_ids

print(part1())
print(part2())
