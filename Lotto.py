import random

def my_numb():
    numb = [] 
    while len(numb) < 6:
        try:
            given_numb = int(input("Enter your number: "))
        except ValueError:
            print("Number must be an integer")
            continue

        if given_numb < 1 or given_numb > 50:
            print("Wrong number. Please enter a number in range 1-50.")
        elif given_numb in numb:
            print("You already wrote that number. Try something else.")
        else:
            numb.append(given_numb)
    return numb

def win_numb():
    return random.sample(range(1, 51), 6)

print("Enter 6 diffrent numbers in range of 1-50.")
print(my_numb())
print(win_numb())