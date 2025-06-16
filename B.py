def main():
    """
    Определяет максимальное количество очков для очков и зонтов, которые могут быть накоплены за день.

    Входные данные:
        Первая строка содержит целое число n - количество дней.
        Последующие n строк содержат две части: утро и вечер.
        Утро и вечер могут быть 'sun' (солнечно) или 'rain' (дождь).

    Выходные данные:
        Первая строка выводит два числа: максимальное количество очков для очков,
        которые могут быть накоплены за день для A и B соответственно.
        Вторая строка выводит два числа: максимальное количество очков для зонтов,
        которые могут быть накоплены за день для A и B соответственно.
    """
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    A_glasses = []
    B_glasses = []
    A_umbrellas = []
    B_umbrellas = []

    for i in range(1, n + 1):
        parts = data[i].split()
        morn = parts[0]
        eve = parts[1]
        A_glasses.append(1 if morn == 'sun' else 0)
        B_glasses.append(1 if eve == 'sun' else 0)
        A_umbrellas.append(1 if morn == 'rain' else 0)
        B_umbrellas.append(1 if eve == 'rain' else 0)

    # Calculate for glasses
    S1 = 0
    S2 = 0
    G0 = 0
    G1 = 0
    for i in range(n):
        S1 += A_glasses[i]
        term = S1 - S2
        if term > G0:
            G0 = term
        S2 += B_glasses[i]
        term2 = S2 - S1
        if term2 > G1:
            G1 = term2

    # Calculate for umbrellas
    S1 = 0
    S2 = 0
    U0 = 0
    U1 = 0
    for i in range(n):
        S1 += A_umbrellas[i]
        term = S1 - S2
        if term > U0:
            U0 = term
        S2 += B_umbrellas[i]
        term2 = S2 - S1
        if term2 > U1:
            U1 = term2

    print(f"{G0} {G1}")
    print(f"{U0} {U1}")

if __name__ == "__main__":
    main()
