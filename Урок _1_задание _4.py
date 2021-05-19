n = int(input('¬ведите целое положительное число: '))
i = 10
j = n%i
max = j
while n !=0:
    j = n%10
    if max <=j:
        max = j
    n = n//10
 
print('максимальна€ цифра в числе ', max) 