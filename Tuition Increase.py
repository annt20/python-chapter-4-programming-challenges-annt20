tuition_fee = 8000
increasing_rate = 0.03
print('Tuition fee estimated for the next 5 years')
print('__________________________________________')
print('Year\t\t\tEstimated Tuition Fee')
for i in range(1, 6):
    tuition_fee += tuition_fee * increasing_rate
    print(i, '\t\t\t\t\t%.2f' % tuition_fee)
