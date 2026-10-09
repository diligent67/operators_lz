b = int(input("Введите B: "))
q = int(input("Введите Q: "))
n = int(input("Введите N: "))

if q == 1:
    s = b * n
else:
    s = b * (q**n - 1) // (q - 1)

print("Сумма геометрической прогрессии:", s)
