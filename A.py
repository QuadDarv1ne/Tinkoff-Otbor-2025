def main():
    """
    Вычисляет и выводит результат выражения на основе входных данных.

    Входные данные:
        Первая строка содержит целое число n.
        Вторая строка содержит целое число m.

    Выходные данные:
        Выводит результат выражения: 10 * n * m + n + m.
    """
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    m = int(data[1].strip())
    result = 10 * n * m + n + m
    print(result)

if __name__ == '__main__':
    main()
