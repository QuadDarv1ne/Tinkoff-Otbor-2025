def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    m = int(data[1].strip())
    result = 10 * n * m + n + m
    print(result)

if __name__ == '__main__':
    main()