revenue = float(input('������� �������� �������: '))
cost = float(input('������� �������� ������: '))
text = '���������� ��������� �� �������� ������: '
profit = revenue-cost # �������/������
profitability = revenue/cost # ��������������
text = '���������� ��������� �� �������� ������: '
if profit >= 0:
        print(text,  "{:2f} ���. ������� �����".format(profit)) 
        print("�������������� ��������� {:05.2f} ���.".format(profitability))
else:
    print(text, "{:2f} ���. ������ �����".format(profit))
chtat = float(input('������� �������� ����������������� �����������: '))
print("������� � ������� �� 1 ���������� ��������� {:05.2f} ���.".format(profit/chtat))
