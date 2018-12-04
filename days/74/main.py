from game import Roll


def main():

    Player_1 = Roll('Dan')
    Player_2 = Roll('Neil')

    print(f'{Player_1.name} Rolls: {Player_1.roll_result}\n{Player_2.name} Rolls: {Player_2.roll_result}')

    print()

    print(determine_who_wins(Player_1, Player_2))


def determine_who_wins(Player_1, Player_2):

    if Player_1.roll_result == Player_2.roll_result:
        return('Its a tie!')
    elif Player_2.roll_result != Player_1.roll_defeat():
        return(
            f'{Player_1.name} wins because {Player_1.roll_result} beats {Player_2.roll_result}!')
    elif Player_1.roll_result != Player_2.roll_defeat():
        return(
            f'{Player_2.name} wins because {Player_2.roll_result} beats {Player_1.roll_result}!')


if __name__ == "__main__":
    main()
