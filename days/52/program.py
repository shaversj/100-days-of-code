import random

word_list = []
correct_guess_set = set()
incorrect_guess_set = set()


def main():

    load_dictionary()
    secret_word = random_word()

    print('Welcome to Hangman!')
    print('_ ' * len(secret_word))
    # Not needed..Just to make each letter easier to read when debugging.
    soup = list(secret_word)
    print(list(soup))

    x = 6
    while x != 0:
        print()
        print(correct_guess_set)
        print(incorrect_guess_set)
        print(f'You have {x} guesses left!')

        guess = input('Guess your letter: '"")
        guess = guess.upper()

        if guess in correct_guess_set or guess in incorrect_guess_set:
            print()
            print('You already picked that letter. Please try again.')
            print()
            x += 1
        elif secret_word.find(guess) != -1:
            correct_guess_set.add(guess)
        elif incorrect_guess_set.add(guess):
            print('Not found. Please try again!')

        for char in secret_word:
            if char in correct_guess_set:
                print(f'{char} ', end="")
            else:
                print('_ ', end="")

        if correct_guess_set == set(secret_word):
            print()
            print(
                f'You guessed all of the letters! The correct word is {secret_word}')
            answer = input('Do you want to play again? (Yes or No) '"")
            answer = answer.lower()
            if answer == 'Yes':
                correct_guess_set.clear()
                incorrect_guess_set.clear()
                main()
        else:
            x -= 1
            continue


def load_dictionary():
    with open('sowpods.txt') as f:
        data = f.readlines()
        for word in data:
            word_list.append(word)


def random_word():
    random_word = random.choice(word_list)
    return random_word.strip()


if __name__ == '__main__':
    main()
