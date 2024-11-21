def custom_write(file_name, strings):
    strings_positions = {}
    number_string = 0
    file = open(file_name, 'w')
    for string in strings:
        line_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(number_string, line_byte)] = string
        number_string += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

