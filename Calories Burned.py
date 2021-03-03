print('Chart of number calories burned')
print('****************************')
print('Minutes\t\t\tCalories')
calories_burned_per_minute = 4.2
total_calories_burned = 0
for i in [10, 15, 20, 25, 30]:
    total_calories_burned = i * calories_burned_per_minute
    print(i, '\t\t\t\t', total_calories_burned)
