n = int(input('������� ����� ������������� �����: '))
i = 10
j = n%i
max = j
while n !=0:
    j = n%10
    if max <=j:
        max = j
    n = n//10
 
print('������������ ����� � ����� ', max) 