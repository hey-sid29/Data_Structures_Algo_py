"""Stack Problem statement 2:
     Convert Integer(base 10) to Binary(Base 2)
     
     example: 242
     242 // 2 = 121 -> 0
     121 // 2 = 60 -> 1
     60 // 2 = 30 -> 0
     30 // 2 = 15 -> 0
     15 // 2 = 7 -> 1
     7 // 2 = 3 -> 1
     3 // 2 = 1 -> 1
     1 // 2 = 0 -> 1
    
    Thus binary equivalent of 242(base 10) = 11110010"""


from Stack_ds import Stack
    
def int_to_bin(int_num):
    s = Stack()

    while int_num>0: #loop goes uptil int_num == 0
        rem = int_num % 2
        int_num = int_num // 2
        s.push(rem)
        #Stack will hold all the remainders from division

    bin_num = "" #stores the binary equivalent of the passed integer num

    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num
#int_num = input("Enter an integer number: ")
print(f"Binary equivalent of {242}: ", int_to_bin(242))