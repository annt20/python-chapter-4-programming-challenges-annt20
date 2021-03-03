print('Miles\t\t\tKilometers')
print('__________________________')
start_point = 10
end_point = 81
increment = 10
rate = 1.60934
for i in range(start_point, end_point, increment):
    print(i, '\t\t\t\t', '%.2f' % (i*rate))
