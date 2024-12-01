data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(struct):
    summ = 0
    if isinstance(struct, (tuple, list, set)):
        for item in struct:
            summ += calculate_structure_sum(item)
    elif isinstance(struct, dict):
        for key, value in struct.items():
            summ += calculate_structure_sum(key) + calculate_structure_sum(value)
    elif isinstance(struct, str):
        return len(struct)
    elif isinstance(struct, (int, float)):
        return struct
    return  summ



result = calculate_structure_sum(data_structure)
print(result)
