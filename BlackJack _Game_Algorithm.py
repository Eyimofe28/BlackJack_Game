import random


def s_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    return random.choice(cards)


def scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def comparison(person, machine):
    if person == machine:
        print("It's a draw.\n")
    elif machine == 21:
        print("Opponent has a BlackJack.\nYou lose!\n")
    elif person == 21:
        print("You win with a BlackJack!!!\n")
    elif person > 21:
        print("You went over. You lose!\n")
    elif machine > 21:
        print("Opponent went over. You win!!\n")
    elif person > machine:
        print("You win!!\n")
    elif machine > person:
        print("You lose!!!\n")


def play_game():
    user = []
    computer = []

    for _ in range(2):
        user.append(s_cards())
        computer.append(s_cards())
    user_score = 0
    computer_score = 0

    continue_game = True
    while continue_game:
        user_score = scores(user)
        computer_score = scores(computer)

        print(f'Your cards: {user}, current score: {user_score}')
        print(f"Computers first card: {computer[0]}.\n")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            continue_game = False
        else:
            redraw = input("Type 'y' to get another card, type 'n' to pass: ")
            if redraw == 'y':
                user.append(s_cards())
            elif redraw == 'n':
                continue_game = False
            else:
                continue_game = False
                print("You did not select a defined option.")

    while computer_score != 21 and computer_score < 19 and len(computer) != len(user):
        computer.append(s_cards())
        computer_score = scores(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}\n")
    comparison(user_score, computer_score)


Gaming = True
while Gaming:
    play = input("Do you want to play a game of BlackJack?\nType 'y' or 'n': ")
    if play == 'y':
        play_game()
    elif play == 'n':
        print('Thank you for playing.\nGoodbye!')
        Gaming = False
    else:
        print('You did not select a defined option.\nGame Over.')
        Gaming = False
