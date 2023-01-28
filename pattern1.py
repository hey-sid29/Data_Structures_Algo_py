"""For a given integer N, print numbers in following pattern
    If N=5
    
    pattern to be printed:
    1
    1 1
    1 1 1
    1 1 1 1
    1 1 1 1 1 """


def print_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print(1, end=' ')
        print("\n")

print_pattern(5)