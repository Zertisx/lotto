import random

def my_numb():
    numb = [] 
    for _ in range(6):
        while 0==0:
            try:
                given_numb = int(input("Enter a number in range 1-50: "))
                if given_numb <= 50 and given_numb > 0:
                    numb.append(given_numb)
                    break
                else:
                    print("Wrong number. Please make sure to type number in range of 1-50. ")
            except ValueError:
                print("Number must be integer")
    return numb

def win_numb():
    numb = []
    for _ in range(6):
        numb.append(random.randint(1,50))
    return numb


print(my_numb())
print(win_numb())