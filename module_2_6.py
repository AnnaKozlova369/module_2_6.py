def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['cat', 123, True]
values_dict = {'a': 4, 'b': True, 'c': 'dog'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['hedgehog', 555]
print_params(*values_list_2, 42) #работает