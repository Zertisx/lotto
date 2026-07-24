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

def win_money(player, winning):
    hit = len(set(player) & set(winning))
    return int(50 * (hit ** 3))

print("Enter 6 diffrent numbers in range of 1-50.")
player_numb = my_numb()
winning_numb = win_numb()
print(player_numb)
print(winning_numb)
print(f"You won: {win_money(player_numb, winning_numb)}")