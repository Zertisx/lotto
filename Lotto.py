def my_numb():
    numb = [] 
    for i in range(6):
        while 0==0:
            given_numb = int(input("Enter a number in range 1-50: "))
            if given_numb <= 50 and given_numb > 0:
                numb.append(given_numb)
                break
            else:
                print("Wrong number. Please make sure to type number in range of 1-50. ")
    return numb

for i in range(6):
    print(my_numb())