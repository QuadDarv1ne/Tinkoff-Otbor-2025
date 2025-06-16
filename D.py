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
    str: Наибольшее "особое" число, составленное из доступных цифр. Если составить число невозможно,
         возвращает пустую строку.
    """
    total = sum(digits_count)
    if total == 0:
        return ""
    count = digits_count[:]
    result = []
    last = None

    while total > 0:
        found = False
        for d in range(9, -1, -1):
            if count[d] == 0:
                continue
            if d == last:
                continue
            count[d] -= 1
            if total == 1:
                result.append(str(d))
                total -= 1
                last = d
                found = True
                break

            max_cnt = max(count)
            if max_cnt <= total // 2:
                result.append(str(d))
                total -= 1
                last = d
                found = True
                break
            else:
                count[d] += 1

        if not found:
            break

    if total > 0:
        return ""
    else:
        return ''.join(result)

def main():
    """
    Основная функция программы.

    Считывает входные данные, представляющие количество доступных цифр от 0 до 9,
    и выводит наибольшее "особое" число, которое можно составить из этих цифр.
    """
    data = input("Введите количество цифр от 0 до 9 через пробел: ").split()
    digits_count = list(map(int, data))
    print(max_special_number(digits_count))

if __name__ == "__main__":
    main()
