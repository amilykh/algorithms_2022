"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def input_number():
    try:
        number = int(input("Введите натуральное число: "))
    except ValueError:
        print("Вы вместо числа ввели строку. Исправьтесь!")
        return input_number()
    return number


def even_odd_digits(number, even=0, odd=0):
    """Рекурсивная функция"""
    # все цифры извлечены
    if number == 0:
        return even, odd
    else:
        current = number % 10
        if not current % 2:
            even += 1
        else:
            odd += 1
        number = number // 10
        return even_odd_digits(number, even, odd)


if __name__ == "__main__":
    number1 = input_number()
    print(f"Количество четных и нечетных цифр в числе равно: {even_odd_digits(number1)}")
