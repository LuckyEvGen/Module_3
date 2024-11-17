def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print('----- Part 1 ------')
print_params()
print_params(b=25)  # Worked but expected type 'str', got 'int' instead
print_params(c=[1, 2, 3])  # Worked but expected type 'bool', got 'List[int]' instead

print('----- Part 2 ------')
values_list = [1, 'string', True]
values_dict = {'a': True, 'b': 777, 'c': 'String'}
print_params(*values_list)
print_params(**values_dict)

print('----- Part 3 ------')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)