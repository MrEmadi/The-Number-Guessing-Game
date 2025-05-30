from art import logo_of_the_app

if __name__ == '__main__':
    try:
        print(logo_of_the_app)
        print('Welcome to The Number Guessing Game!')
        print('\nI\'m thinking of a number between 1 and 100')
        user_level = input("Choose difficulty. Type 'easy' or 'hard': ")
        levels = {
            'easy': 10,
            'hard': 5
        }
        if not user_level in levels:
            raise Exception('Invalid difficulty level! Try again later.')
        chances = levels[user_level]
        print(f"You have {chances} attempts remaining to guess the number.")
    except Exception as e:
        print(f'\nError -> {e}')
