import random

def print_tic_tac_toe(pos1='1', pos2='2', pos3='3', pos4='4', pos5='5', pos6='6', pos7='7', pos8='8', pos9='9', current_player=None):
    print("\n")
    print(f'{current_player}\'s Turn')
    
    print("\t     |     |")
    print(f"\t  {pos1}  |  {pos2}  |  {pos3}")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print(f"\t  {pos4}  |  {pos5}  |  {pos6}")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print(f"\t  {pos7}  |  {pos8}  |  {pos9}")
    print("\t     |     |")
    print("\n")


player_1 = input('Enter player 1\'s name:   ')
player_1_symbol = ''
player_2 = input('Enter player 2\'s name:   ')
player_2_symbol = ''
players = []


players.append(player_1)
players.append(player_2)

current_players_turn = random.choice(players)

print(f'Randomly choosing player to go.......')
print(f'{current_players_turn} has been selected to go first.')

player_symbol = input(f'Hey {current_players_turn}, Do you want to be X or O?    ')

if player_symbol == 'x' or player_symbol == 'X':
    player_1_symbol += 'X'
    player_2_symbol += 'O'
elif player_symbol == 'o' or player_symbol == 'O':
    player_1_symbol += 'O'
    player_2_symbol += 'X'
else:
    print('Not a valid selection')



print(f'Time to select a location, {current_players_turn}.....')


print_tic_tac_toe(current_players_turna)


selected_position = int(input('Which location do you want to go to?          '))




if selected_position == 1:
    if current_players_turn == player_1:
        pos1 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos1 = player_2_symbol
        current_players_turn = player_1

if selected_position == 2:
    if current_players_turn == player_1:
        pos2 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos2 = player_2_symbol
        current_players_turn = player_1

if selected_position == 3:
    if current_players_turn == player_1:
        pos3 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos3 = player_2_symbol
        current_players_turn = player_1

if selected_position == 4:
    if current_players_turn == player_1:
        pos4 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos4 = player_2_symbol
        current_players_turn = player_1

if selected_position == 5:
    if current_players_turn == player_1:
        pos5 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos5 = player_2_symbol
        current_players_turn = player_1

if selected_position == 6:
    if current_players_turn == player_1:
        pos6 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos6 = player_2_symbol
        current_players_turn = player_1

if selected_position == 7:
    if current_players_turn == player_1:
        pos7 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos7 = player_2_symbol
        current_players_turn = player_1

if selected_position == 8:
    if current_players_turn == player_1:
        pos8 = player_1_symbol
        current_players_turn = player_2
        print_tic_tac_toe
    elif current_players_turn == player_2:
        pos8 = player_2_symbol
        current_players_turn = player_1

if selected_position == 9:
    if current_players_turn == player_1:
        pos9 = player_1_symbol
        current_players_turn = player_2
    elif current_players_turn == player_2:
        pos9 = player_2_symbol
        current_players_turn = player_1

print_tic_tac_toe(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, current_players_turn)