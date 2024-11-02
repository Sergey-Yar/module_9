first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f[0]) - len(f[1]) for f in zip(first, second) if len(f[0]) != len(f[1]))

second_result = (len(first[s]) == len(second[s]) for s in range(len(first)))

print(list(first_result))
print(list(second_result))