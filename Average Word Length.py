input_value = 0
total_value_length = 0
count = 0
while input_value != '':
    input_value = input('Enter a word (Press ENTER to exit): ')
    count += 1
    for i in input_value:
        total_value_length += 1
print('The average length of the words entered: ', round(total_value_length / count))
