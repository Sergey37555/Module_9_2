first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(a) for a in first_strings if len(a) >= 5]
second_result = [(b, a) for b in first_strings for a in second_strings if len(b) == len(a)]
third_result = {a: len(a) for a in first_strings + second_strings if len(a) % 2 == 0}

## Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)