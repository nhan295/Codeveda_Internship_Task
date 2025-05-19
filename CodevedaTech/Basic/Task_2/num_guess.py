import random

while True:
    num_guess = input('Type a range number to guess: ')

    if num_guess.isdigit():
        num_guess = int(num_guess)
        if num_guess > 0:
            break
        else:
            print('Please type a number larger than 0')
    else:
        print('Please type a valid number')
        
random_num  = random.randint(0,num_guess)
guess_time = 0

while True: 
    guess_time += 1
    user_guess = input('Make a guess:  ')

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print('Please type a number')
        continue

    if user_guess == random_num:
        print('You got it')
        break
    elif user_guess < random_num:
        print('Guess higher number')
    else: 
        print('Guess lower number')
print('You got it in',guess_time,"guesses")