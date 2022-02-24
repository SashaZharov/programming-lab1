import re

#numbers = "-1, 2, 3,134, 4, 5, 6, 7, 13 + i, -2+3j, 3/5"
numbers = input()

Nat = []  # Натуральные числа +
Int = []  # Целые числа +
Rat = []  # Рациональные +
Real = []  # Вещественные +
Com = []  # Комплексные +
Even = []  # Четные
Odd = []  # Нечетные
Sim = []  # Простые +


def isSim(i):
    n = int(i)
    lst = []
    for i in range(2, n+1):
        # пробегаем по списку (lst) простых чисел
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def Sort(num):

    Num = [i for i in num.split(", ")]
    print(Num)
    for i in Num:
        # Вещественные числа
        if re.fullmatch(r'[\s]*[-+]?(?:\d+(?:\.|\,\d*)|\.|\,\d+)(?:[eE][-+]?\d+)??', i):
            Real.append(i)
            Rat.append(i)
            #print("Real", Real)

        # Целые числа
        if re.fullmatch(r'[\s]*[-+]?\d+', i):
            Int.append(i)
            Rat.append(i)
            #print("Int", Int)

            # Натуралтные числа
            if re.fullmatch(r'[\s]*[+]?\d+', i):
                Nat.append(i)
                #print("Nat", Nat)

        # комплексные числа
        if re.fullmatch(r'[\s]*[-+]?\d*[\s]*[+-][\s]*\d*[ij]', i):
            Com.append(i)
            #print("Com", Com)

        # рациональные числа
        if re.fullmatch(r'[\s]*[-+]?\d*[\s]*/[\s]*\d*', i):
            Rat.append(i)
            #print("Rat", Rat)


Sort(numbers)

# Простые
# Четные/нечетные
for i in Int:
    if isSim(i):
        Sim.append(i)
        #print("Sim", Sim)
    if int(i) % 2 != 0:
        Odd.append(i)
    else:
        Even.append(i)


print("Nat ", Nat, "\nInt ", Int, "\nRat ", Rat, "\nReal ", Real,
      "\nCom ", Com, "\nEven ", Even, "\nOdd", Odd, "\nSim", Sim)
