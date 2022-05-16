# 31 Составить список простых множителей натурального числа N

N = int(input('Введите натуральное число N: '))
List = []
for i in range(2, N):
    while N % i == 0:
        List.append(i)
        N = N / i
    if N == 1:
        break

if len(List) == 0:
    print('Число является простым')
else:
    print(f'Список множителей числа N:', List)