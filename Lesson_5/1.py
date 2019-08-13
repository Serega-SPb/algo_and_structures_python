"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple


enterprise = namedtuple('Enterprise', 'Name Q1 Q2 Q3 Q4')
enterprises = []
ent_count = int(input("Введите кол-во предприятий: "))

for e in range(ent_count):

    name = input('Введите наименование: ')
    quarters = input('Введите квартальную(1-4) прибыль через " ": ')
    quarters_float = [float(x) for x in quarters.split()]
    enterprises.append(enterprise(name, *quarters_float[:4]))

aver_profit = namedtuple('Average_profit', 'Enterprise Value')
aver_profits = []

for ent in enterprises:
    sum_profits = 0
    for i in range(1, 5):
        sum_profits += ent[i]
    aver_profits.append(aver_profit(ent.Name, sum_profits/4))

average = sum(ap.Value for ap in aver_profits) / len(aver_profits)

# print(aver_profits)
# print(average)


more_aver = []
less_aver = []

for avr in aver_profits:
    if avr.Value > average:
        more_aver.append(avr.Enterprise)
    elif avr.Value < average:
        less_aver.append(avr.Enterprise)

print('Предприятия с прибылью выше средней: ')
print(', '.join(more_aver))
print('-'*50)
print('Предприятия с прибылью ниже средней: ')
print(', '.join(less_aver))
print('-'*50)
