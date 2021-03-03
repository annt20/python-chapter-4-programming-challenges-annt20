total = 0
for i in range(1, 6):
    bugs_collected = int(input('Enter the bugs collected for day %d: ' % i))
    total += bugs_collected
print('The total bugs collected in five days: ', total)
