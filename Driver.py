#This program contains three related modules.

# 2 players will play the game

import Trivia_Questions

ques = Trivia_Questions.Triv_Ques()
len_list = len(ques)

turn = 0

score_player1 = 0
score_player2 = 0

for i in range(len_list):
    if (turn % 2) == 0:
        print('Question for the first player:')
        print(ques[i])
        ans = int(input('Enter your solution (a number between 1 and 4): '))
        if ans == ques[i].getNumberForCorrectAnswer():
            print('That is the correct answer.')
            score_player1 += 1
        else:
            print(f'That is incorrect. The correct answer is {ques[i].getNumberForCorrectAnswer()}')


    else:
        print('Question for the second player:')
        print(ques[i])
        ans = int(input('Enter your solution (a number between 1 and 4): '))
        if ans == ques[i].getNumberForCorrectAnswer():
            print('That is the correct answer.')
            score_player2 += 1
        else:
            print(f'That is incorrect. The correct answer is {ques[i].getNumberForCorrectAnswer()}')

    turn += 1

print()
print(f'The first player earned {score_player1} points.')
print(f'The second player earned {score_player2} points.')

#Result
if score_player1 > score_player2:
    print('The first player wins the game.')
elif score_player1 < score_player2:
    print('The second player wins the game.')
else:
    print('The first player tied with the second player.')

