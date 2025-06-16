def max_special_number(digits_count):
    """
    Создает наибольшее "особое" число из доступных цифр, где никакие две соседние цифры не одинаковы.

    Функция принимает список, содержащий количество доступных цифр от 0 до 9, и возвращает
    наибольшее число, которое можно составить из этих цифр, соблюдая условие, что никакие
    две соседние цифры не являются одинаковыми.

    Параметры:
    digits_count (list): Список из 10 целых чисел, где каждый элемент представляет количество
                         доступных цифр от 0 до 9.

    Возвращает:
    str: Наибольшее "особое" число, составленное из доступных цифр.

    Пример:
    >>> max_special_number([2, 3, 0, 0, 0, 0, 0, 0, 0, 0])
    '10101'
    """
    result = []
    last_digit = None

    while True:
        added = False
        for digit in range(9, -1, -1):
            if digits_count[digit] > 0 and digit != last_digit:
                result.append(str(digit))
                digits_count[digit] -= 1
                last_digit = digit
                added = True
                break

        if not added:
            break

    return ''.join(result)

# Пример использования
input_data = input().strip()
digits_count = list(map(int, input_data.split()))
print(max_special_number(digits_count))
