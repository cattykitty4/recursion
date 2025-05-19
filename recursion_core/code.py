def get_recursion(data):
    if data == 1:  # базовый случай
        return 1

    else:  # рекурсивный случай
        return get_recursion(data - 1) * data

# Рекурсия 1: data = 5, else: get_recursion(4) * 5  Результат: 24 * 5 = 120
# Рекурсия 2: data = 4, else: get_recursion(3) * 4  Результат: 6 * 4 = 24
# Рекурсия 3: data = 3, else: get_recursion(2) * 3  Результат: 2 * 3 = 6
# Рекурсия 4: data = 2, else: get_recursion(1) * 2  Результат: 1 * 2 = 2
# Рекурсия 5: data = 1, if: return 1,               Результат: 1
