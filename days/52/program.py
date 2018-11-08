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

    while True:
        print()
        print(correct_guess_set)
        print(incorrect_guess_set)
        guess = input('Guess your letter: '"")
        guess = guess.upper()

        if secret_word.find(guess) != -1:
            correct_guess_set.add(guess)
        else:
            incorrect_guess_set.add(guess)
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
            break
        else:
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
