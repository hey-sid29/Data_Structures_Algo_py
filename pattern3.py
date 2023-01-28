"""for an integer n, obtain following pattern


    if n=4:
        pattern:
            
            1
            2 3
            3 4 5
            4 5 6 7"""

def get_pattern(n):
    x=0
    for i in range(n):
        x = i+1
        for j in range(i+1):
            print(x, end='')
            x=x+1
        print('\n')

get_pattern(4)