value = int(input('Enter a positive integer: '))
factorial = 1
while value <= 0:
    value = int(input('Enter a positive integer (greater than 0): '))
for i in range(1, value+1):
    factorial *= i
print(value, '! = ', factorial)
