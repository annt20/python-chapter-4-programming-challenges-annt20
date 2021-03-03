starting_number_of_organism = int(input('Enter the starting number of organism: '))
daily_increase_rate = float(input('Enter the average daily increase (%): '))
days_to_multiply = int(input('Enter number of days to multiply: '))
population = starting_number_of_organism
print('Day Approximate\t\t\tPopulation')
print('++++++++++++++++++++++++++++++++++')
print('1\t\t\t\t\t\t   ', population)
for i in range(2, days_to_multiply+1):
    population = population + ((daily_increase_rate/100) * population)
    print(i, '\t\t\t\t\t\t\t%.3f' % population)
