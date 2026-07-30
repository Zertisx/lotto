import random

def get_player_numbers():
    numb = [] 
    while len(numb) < 6:
        try:
            given_numb = int(input("Enter your number: "))
        except ValueError:
            print("Number must be an integer")
            continue

        if given_numb < 1 or given_numb > 49:
            print("Wrong number. Please enter a number in range 1-49.")
        elif given_numb in numb:
            print("You already wrote that number. Try something else.")
        else:
            numb.append(given_numb)
    return numb

def is_valid_numbers(numbers):
    if len(numbers) != 6:
        return (False, "You must enter exactly 6 numbers.")
    checked = []
    for given_numb in numbers:
        if not given_numb.isdigit():
            return (False, "Please enter whole numbers only.")
        n = int(given_numb)
        if n < 1 or n > 49:
            return (False, "Numbers must be in range 1-49.")
        if n in checked:
            return (False, "No duplicate numbers allowed")
        checked.append(n)  
    return (True, "")

def get_winning_numbers():
    return random.sample(range(1, 50), 6)

def calculate_prize(player, winning):
    prizes = [0, 0, 50, 170, 2000, 5000, 20000 ]
    hit = len(set(player) & set(winning))
    return prizes[hit]


def main():
    print("Enter 6 different numbers in range of 1-49.")
    player_numb = get_player_numbers()
    winning_numb = get_winning_numbers()
    print(player_numb)
    print(winning_numb)
    print(f"You won: {calculate_prize(player_numb, winning_numb)}")


if __name__ == '__main__':
    main()