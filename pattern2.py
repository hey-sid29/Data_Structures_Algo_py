"""For an integer N, print the following pattern:
 
 if n=4
 pattern:

     1234
     123
     12
     1"""


def get_pattern(n):

    for i in range(n,0, -1):
        for  j in range (1, i+1):
            print(j, end="")
        print("\n")


get_pattern(4)