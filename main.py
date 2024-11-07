# '1st program'
print(9**0.5*5)

# '2nd program'
# Дано 4 числа
n1=9.99
n2=9.98
n3=1000
n4=1000.1
print(n1>n2, n3!=n4 )

# 3rd program

# Дано два целых четырёхзначных числа
num1 = 1234
num2 = 5678

# Извлекаем серединные числа
middle_num1 = (num1 // 10) % 100  # 23
middle_num2 = (num2 // 10) % 100  # 67

# Вычисляем сумму серединных чисел
sum_middle = middle_num1 + middle_num2

# Выводим результат на экран
print("Сумма серединных чисел:", sum_middle)

# 4th program

# Дано два дробных числа
num1 = 13.42
num2 = 42.13

# Получаем целые и дробные части
int_part_num1 = int(num1)
frac_part_num1 = int((num1 - int_part_num1) * 100)  # умножаем на 100, чтобы получить дробную часть
int_part_num2 = int(num2)
frac_part_num2 = int((num2 - int_part_num2) * 100)

# Проверяем условия
if int_part_num1 == frac_part_num2 or int_part_num2 == frac_part_num1:
    print("Целая часть хотя бы одного числа равна дробной части другого.")
else:
    print("Целая часть не равна дробной части другого числа.")




