from random import randint

exact_number = randint(1, 101)
guess = input("Enter guess: ")
guess = int(guess)
count = 1
list = []
if (guess < 1 or guess > 100):
    print("Out of Bounds!")
elif (guess >= exact_number - 10 and guess <= exact_number + 10):
    print("WARM!")
elif (guess <= exact_number - 10 or guess >= exact_number + 10):
    print("COLD!")
list.append(guess)
while (guess != exact_number):
    count += 1
    guess_again = input("Enter the guess again: ")
    guess_again = int(guess_again)
    if (guess_again == exact_number):
        break
    elif (guess_again < 1 and guess_again > 100):
        print("Out of Bounds!")

    elif (abs(exact_number - guess_again) <= abs(exact_number - list[-1])):
        print("WARMER!")
    elif (abs(exact_number - guess_again) >= abs(exact_number - list[-1])):
        print("COLDER!")

    list.append(guess_again)

print(f"You have guessed correctly. The number of tries you took are: {count} all your recorded tries are {list}")