import random
print("====================================")
random_numbers = [random.uniform(0,1) for _ in range(8)]
print(random_numbers)
print("====================================")

##b
print("====================================")
k = int(input("Введите количество случайных чисел: "))
random_numbers = [random.uniform(0,1) for _ in range(k)]
print(random_numbers)
print("====================================")

##v
print("====================================")
random_numbers = [random.uniform(25, 26) for _ in range(15)]
for number in random_numbers:
    print(number)
print("====================================")
##g
print("====================================")
a = int(input("Введите значение a: "))
b = float(input("Введите значение b: "))
k = random.randint(1, a)
random_numbers = [random.uniform(0, b) for _ in range(k)]
print(f"Случайное натуральное число k: {k}")
print("Случайные вещественные числа:")
for number in random_numbers:
    print(number)
    print("====================================")

    ##d
random_numbers = [random.uniform(-40, 40) for _ in range(10)]
for number in random_numbers:
    print(number)
    print("====================================")
    ##e
    print("====================================")
random_numbers = [random.uniform(0, 15) for _ in range(15)]
for number in random_numbers:
    print(number)
print("====================================")

#z
print("====================================")
import random
a = int(input("Введите значение a: "))
b = float(input("Введите значение b: "))
m = int(input("Введите значение m: "))
k = random.randint(1, m)
random_numbers = [random.uniform(0, b) for _ in range(k)]
print(f"Случайное натуральное число k: {k}")
print("Случайные вещественные числа:")
for number in random_numbers:
    print(number)
    print("====================================")
