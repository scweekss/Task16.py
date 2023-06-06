s = int(input('Сумма чисел \n'))
p = int(input('Произведение чисел \n'))
for a in range(s):
    for b in range(p):
        if s == a + b and p == a * b:
            print(f'первое число ="{a}", второе число ="{b}"')
