from art import logo_of_the_app
from random import randint

if __name__ == '__main__':
    print(logo_of_the_app)
    print('Welcome to The Number Guessing Game!')
    print('\nI\'m thinking of a number between 1 and 100')
    user_level = input("Choose difficulty. Type 'easy' or 'hard': ")
    levels = {
            'easy': 10,
            'hard': 5
        }
    while not user_level in levels:
        user_level = input("Try again! Choose difficulty. Type 'easy' or 'hard': ")
    chances = levels[user_level]
    random_number_1_to_100 = randint(1, 100) # [1, 100]
    while chances > 0:
        try:
            print(f"You have {chances} attempts remaining to guess the number.")
            user_guess = int(input('\nMake a guess: '))
            if not 1 <= user_guess <= 100:
                raise Exception('Guess must be a number between 1 and 100')
            chances -= 1
            diff_number = user_guess - random_number_1_to_100
            if diff_number == 0:
                print(f'You got it! '
                      f'The answer was {random_number_1_to_100}')
                print('\nBye!')
                break
            if chances == 0:
                print('You\'ve run out of guesses! You lose.')
                print('\nBye!')
                break
            result_diff = "High" if diff_number < 0 else "Low"
            print(f'{result_diff}! Guess again.\n')
        except ValueError:
            print('\nError -> You must enter a number! Try again.\n')
        except Exception as error:
            print(f'\nError -> {error}! Try again.\n')
