a, b = map(int, input().split())
proverka = (-10e9 <= a <= 10e10 and -10e9 <= b <= 10e9)
kolvo = 0
while proverka == False and kolvo < 2:
    print('Попробуйте еще раз')
    kolvo += 1
    a, b = map(int, input().split())
    proverka = (-10e9 <= a <= 10e10 and -10e9 <= b <= 10e9)
    if kolvo == 3:
        break
else:
    print(a + b)