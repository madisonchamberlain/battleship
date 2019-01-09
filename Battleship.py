
import random

# gets valid int (works as it should)
def valid_seed(seed):
    if seed.lstrip('-').isdigit():
        return True
    return False

# gets a valid int over zero (works as it should)
def valid_int_over_zero(num):
    if num.isdigit() and (int(num) > 0):
        return True
    return False

# gets a number between 0 and 3 for the AI (works as it should)
def num_between_1_and_3(num):
    if num.isdigit() and int(num) <= 3 and int(num) >= 1:
        return True
    return False

# finds out if a move has already been done and is within the board (works as it should)
def is_valid_move(user_move, board):
    user_move_list = user_move.split(' ')
    if len(user_move_list) == 2:

        row, col = user_move_list
        row = row.strip()
        col = col.strip()
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            if (0 <= row) and (row < len(board)) and (0 <= col) and (col < len(board[0])):
                return board[row][col] != 'X' and board[row][col] != 'O'
            else:
                #print('first else')
                return False
    else:
        #print('second else')
        return False

#updates game state for any piece and location and onto any board (works as it should)
def update_game_state(piece_to_place, move_row, move_col, board_to_be_updated):
    board_to_be_updated[move_row][move_col] = piece_to_place
    return board_to_be_updated

# displays the board as a board rather than as a list (works as it should)
def display_game_state(board: list):
    print(' ',end=' ')
    for col_num in range(len(board[0])):

        print(col_num,'', end = ' '*2)
    print()
    for row_num, row in list(enumerate(board)):

        print(row_num, end = ' ')
        row_image = ('   '.join(row))
        print(row_image)

# sets the board and finds out if it is a diaganol (works as it should)
def set_board(row1, row2, col1, col2):
    list_of_possible_coordinates = []
    if row1 == row2 and col1 == col2:
        ship = [(row1, col1)]
        return ship
    else:
        if (int(col1) != int(col2)) and (int(row1) == int(row2)):
            cols = range(min(col1, col2), max(col1, col2) + 1)
            for col in cols:
                ship_piece = (row1, col)
                list_of_possible_coordinates.append(ship_piece)
        elif int(col1) == int(col2) and int(row1) != int(row2):
            rows = range(min(row1, row2), max(row1, row2) + 1)
            for row in rows:
                ship_piece = (row, col1)
                list_of_possible_coordinates.append(ship_piece)
        elif (col1 != col2) and (row1 != row2):
            print("Ships cannot be placed diagonally. Terminating game.")
            exit(0)
    return list_of_possible_coordinates

# makes a blank board (works as it should)
def make_board(num_rows: int, num_cols: int, blank_char: str) -> list:
    board = []
    for row_number in range(num_rows):
        row = [blank_char] * num_cols
        board.append(row)
    return board

# places the user ship (works as it should)
def ship_location_dictionary(file_name, row_input, col_input):
    dict_of_moves = {}
    list_of_symbols = []
    list_of_moves = []
    with open(file_name, encoding='utf-8-sig') as file:
        for line in file:
            line = line.split(" ")
            symbol = line[0]
            row1 = int(line[1])
            col1 = int(line[2])
            row2 = int(line[3])
            col2 = int(line[4])
            s_row = min(row1, row2)
            l_row = max(row1, row2)
            s_col = min(col1, col2)
            l_col = max(col1, col2)
            coordinates = set_board(row1, row2, col1, col2)
            if symbol in list_of_symbols:
                print("Error symbol", symbol, "is already in use. Terminating game")
                exit(0)
            else:
                list_of_symbols.append(symbol)
                symbol = symbol
            if (symbol == "x") or (symbol == "X") or (symbol == "o") or (symbol == "O") or (symbol == "*"):
                print ("Please do not use that symbol. Terminating game.")
                exit(0)
            else:
                list_of_symbols.append(symbol)
                symbol = symbol
            if (s_row < 0) or (s_col < 0) or (l_row > col_input - 1) or (l_col > row_input - 1):
                print("Error", symbol, "is placed outside of the board. Terminating game.")
                exit(0)
            else:
                list_of_moves.append(coordinates)
                coordinates = coordinates
            dict_of_moves[symbol] = coordinates
        return dict_of_moves

#sets up the user board with the ship coordinates (works as it should)
def user_board(dict_of_user_moves, user_board):
    for symbol, coordinates in dict_of_user_moves.items():
        for coordinate in coordinates:
            board = update_game_state(symbol, coordinate[0], coordinate[1], user_board)
    return board

#this function correctly returns a list of touples of boat size and name
def symbol_and_size_dict(dict_of_user_moves):
    dict_of_symbols_and_boat_size = {}
    for symbol, coordinates in dict_of_user_moves.items():
        boat_length = len(coordinates)
        dict_of_symbols_and_boat_size[symbol] = boat_length
    return sorted(dict_of_symbols_and_boat_size.items())

def is_overlapping(list_of_ships_already_placed, ship_trying_to_place):
    for coordinate in ship_trying_to_place:
        if coordinate not in list_of_ships_already_placed:
            return False

# this function does not work sos ########################################################
def choses_AI_placement(list_of_ships_already_placed, boat_symbol_size, rows, cols):
    dictionary_of_symbols_and_coordinates = {}
    overlaping = True
    while overlaping == True:
        for item in boat_symbol_size:
            coord_of_boat_were_testing = []
            h_or_v = random.choice(["vert", "horz"])
            if h_or_v == "horz":
                max_start_point = cols - item[1]
                start_row = random.randint(0, rows - 1)
                start_col = random.randint(0, max_start_point)
                for number in range(0, item[1]):
                    coordinate = (start_row, start_col)
                    start_col += 1
                    coord_of_boat_were_testing.append(coordinate)
            elif h_or_v == "vert":
                max_start_point = rows - item[1]
                start_row = random.randint(0, max_start_point)
                start_col = random.randint(0, cols - 1)
                coord_of_boat_were_testing = []
                for number in range(0, item[1]):
                    coordinate = (start_row, start_col)
                    start_row += 1
                    coord_of_boat_were_testing.append(coordinate)
            overlapping = is_overlapping(list_of_ships_already_placed, coord_of_boat_were_testing)
            if overlapping == False:
                dictionary_of_symbols_and_coordinates[item[0]] = coord_of_boat_were_testing
        return dictionary_of_symbols_and_coordinates

# puts AI ships in their places (works as it should)
def make_AI_board(dictionary_of_symbols_and_coordinates, board):
    for symbol, coordinates in dictionary_of_symbols_and_coordinates.items():
        for coordinate in coordinates:
            board = update_game_state(symbol, coordinate[0], coordinate[1], board)
    return board

# returns the coordinates of the entire board in order for the random AI (works as it should)
def unfired_options(rows, cols):
    unfired = []
    for i in range(0, cols):
        for j in range(0, rows):
            unfired.append((i, j))
    return unfired

def ai_sinks_user(users_board, dict_ships:dict, already_sunk_by_ai):
    for ship_symbol in dict_ships.keys():
        checker = 0
        for row in users_board:
            if ship_symbol in row:
                checker += 1
        if checker == 0:
            if ship_symbol not in already_sunk_by_ai:
                print('You sunk my', ship_symbol)
                already_sunk_by_ai.append(ship_symbol)
                return True

def user_sinks_ai(ai_board, dict_ships:dict, already_sunk_by_user):
    for ship_symbol in dict_ships.keys():
        checker = 0
        for row in ai_board:
            if ship_symbol in row:
                checker += 1
        if checker == 0:
            if ship_symbol not in already_sunk_by_user:
                print('You sunk my', ship_symbol)
                already_sunk_by_user.append(ship_symbol)
                return True

def random_AI_attack(unfired, users_board, AI_board, dict_of_user_ships, already_sunk_by_user, already_sunk_by_ai):
    coords_to_fire = random.choice(unfired)
    print("The AI fires at location (%d, %d)" % (coords_to_fire[0], coords_to_fire[1]))
    if users_board[coords_to_fire[0]][coords_to_fire[1]] != "*":
        update_game_state("X", coords_to_fire[0], coords_to_fire[1], users_board)
        if (not user_sinks_ai(AI_board, dict_of_user_ships, already_sunk_by_user)) and (not ai_sinks_user(users_board, dict_of_user_ships, already_sunk_by_ai)):
            print("Hit!")
    else:
        update_game_state("O", coords_to_fire[0], coords_to_fire[1], users_board)
        print("Miss!")
    unfired.remove(coords_to_fire)
    #list_of_user_ships.remove(coords_to_fire)
    return coords_to_fire

def AI_coords_to_fire_cheat(dict_of_user_ships):
    coords_to_fire_cheat = []
    for values in dict_of_user_ships.values():
        for tuple in values:
            coords_to_fire_cheat.append(tuple)
    coords_to_fire_cheat.sort()
    return coords_to_fire_cheat

def cheating_AI_attack(coords_to_fire_cheat, dict_of_user_ships, users_board, AI_board, already_sunk_by_user, already_sunk_by_ai):
    cheat_row_choice, cheat_col_choice = coords_to_fire_cheat[0]
    print('The AI fires at location (%d, %d)' % (cheat_row_choice, cheat_col_choice))
    update_game_state("X", cheat_row_choice, cheat_col_choice, users_board)
    coords_to_fire_cheat.remove(coords_to_fire_cheat[0])
    if (not user_sinks_ai(AI_board, dict_of_user_ships, already_sunk_by_user)) and (not ai_sinks_user(users_board, dict_of_user_ships, already_sunk_by_ai)):
        print('Hit!')

def is_valid_smart_move(row_move, col_move, board, cols, rows, spots):
    if row_move >= cols or col_move >= rows or row_move < 0 or col_move < 0:
        return False
    if board[row_move][col_move] == 'X' or board[row_move][col_move] == 'O':
        return False
    for i in range(len(spots)):
        if (row_move, col_move) == spots[i]:
            return False
    return True

def smart_AI_attack(spots, mode, unfired, user_board, rows, cols, dict_of_user_ships, AI_board, already_sunk_by_user, already_sunk_by_ai):
    if mode == 'hunt':
        AI_move = random.choice(unfired)
        print('The AI fires at location (%d, %d)' %(AI_move[0], AI_move[1]))
        if user_board[AI_move[0]][AI_move[1]] != '*':
            user_board[AI_move[0]][AI_move[1]] = 'X'
            if (not user_sinks_ai(AI_board, dict_of_user_ships, already_sunk_by_user)) and (not ai_sinks_user(user_board, dict_of_user_ships, already_sunk_by_ai)):
                print('Hit!')
            move1 = (AI_move[0]-1,AI_move[1])
            if move1 not in unfired:
                spots.append((AI_move[0]-1,AI_move[1]))
            move2 = (AI_move[0]+1,AI_move[1])
            if move2 not in unfired:
                spots.append((AI_move[0]+1,AI_move[1]))
            move3 = (AI_move[0],AI_move[1]-1)
            if move3 not in unfired:
                spots.append((AI_move[0],AI_move[1]-1))
            move4 = (AI_move[0],AI_move[1]+1)
            if move4 not in unfired:
                spots.append((AI_move[0],AI_move[1]+1))
            mode = 'destroy'
            return mode
        else:
            user_board[AI_move[0]][AI_move[1]] = 'O'
            print('Miss!')
            unfired.remove(AI_move)
    else:
        while len(spots) > 0:
            spots.sort()
            AI_move = spots[0]
            #print('IN DESTROY')
            print('The AI fires at location (%d, %d)' %(AI_move[0], AI_move[1]))
            if user_board[AI_move[0]][AI_move[1]] != '*':
                user_board[AI_move[0]][AI_move[1]] = 'X'
                unfired.remove(AI_move)
                spots.pop(0)
            move1 = (AI_move[0] - 1, AI_move[1])
            if move1 not in unfired:
                spots.append((AI_move[0] - 1, AI_move[1]))
            move2 = (AI_move[0] + 1, AI_move[1])
            if move2 not in unfired:
                spots.append((AI_move[0] + 1, AI_move[1]))
            move3 = (AI_move[0], AI_move[1] - 1)
            if move3 not in unfired:
                spots.append((AI_move[0], AI_move[1] - 1))
            move4 = (AI_move[0], AI_move[1] + 1)
            if move4 not in unfired:
                spots.append((AI_move[0], AI_move[1] + 1))
            if (not user_sinks_ai(AI_board, dict_of_user_ships, already_sunk_by_user)) and (not ai_sinks_user(user_board, dict_of_user_ships, already_sunk_by_ai)):
                print('Hit!')
                break
            else:
                user_board[AI_move[0]][AI_move[1]] = 'O'
                spots.pop(0)
                unfired.remove(AI_move)
                print('Miss!')
                break
            # break
        if len(spots) == 0:
            mode = 'hunt'

# returns a list of ship coordinates (works as it should)
def list_of_user_ships(dict_of_moves):
    list_of_user_ships = []
    if dict_of_moves == {'P': [(0, 0)]}:
        list_of_user_ships = [(0, 0)]
        return list_of_user_ships
    else:
        for symbol, coordinates in dict_of_moves.items():
            for coordinate in coordinates:
                list_of_user_ships.append(coordinate)
            return list_of_user_ships

# returns a list of ship coordinates (works as it should)
def list_of_AI_ships(dictionary_of_symbols_and_coordinates):
    list_of_AI_ships = []
    if dictionary_of_symbols_and_coordinates == {'P': [(0, 0)]}:
        list_of_AI_ships = [(0, 0)]
        return list_of_AI_ships
    else:
        for symbol, coordinates in dictionary_of_symbols_and_coordinates.items():
            for coordinate in coordinates:
                list_of_AI_ships.append(coordinate)
                return list_of_AI_ships

def ship_sunk_game_over(list_of_user_ships, scanning_board, users_board, dict_ships, ai_board, already_sunk_by_user, already_sunk_by_ai):
    if len(already_sunk_by_ai) == len(dict_ships.keys()):
        print('Scanning Board')
        display_game_state(scanning_board)
        print()
        print("My Board")
        display_game_state(users_board)
        print()
        print('The AI wins.')
        exit(0)
    if len(already_sunk_by_user) == len(dict_ships.keys()):
        print('Scanning Board')
        display_game_state(scanning_board)
        print()
        print("My Board")
        display_game_state(users_board)
        print()
        print('You win!')
        exit(0)
    for ship_symbol in dict_ships.keys():
        checker = 0
        for row in ai_board:
            if ship_symbol in row:
                checker += 1
        if checker == 0:
            if ship_symbol not in already_sunk_by_ai:
                print('You sunk my', ship_symbol)
                already_sunk_by_ai.append(ship_symbol)
                break
    for ship_symbol in dict_ships.keys():
        checker = 0
        for row in users_board:
            if ship_symbol in row:
                checker += 1
        if checker == 0:
            if ship_symbol not in already_sunk_by_user:
                print('You sunk my', ship_symbol)
                already_sunk_by_user.append(ship_symbol)
                break
    if len(already_sunk_by_ai) == len(dict_ships.keys()):
        print('Scanning Board')
        display_game_state(scanning_board)
        print()
        print("My Board")
        display_game_state(users_board)
        print()
        print('The AI wins.')
        exit(0)
    if len(already_sunk_by_user) == len(dict_ships.keys()):
        print('Scanning Board')
        display_game_state(scanning_board)
        print()
        print("My Board")
        display_game_state(users_board)
        print()
        print('You win!')
        exit(0)
    return False

# just the main function (don't really know if it works until the entire game works)
def main():
    chosen_seed = input('Enter the seed: ')
    while not valid_seed(chosen_seed):
        chosen_seed = input('Enter the seed: ')
    random.seed(int(chosen_seed))
    rows = input('Enter the width of the board: ')
    while not valid_int_over_zero(rows):
        rows = input('Enter the width of the board: ')
    rows = int(rows)
    cols = input('Enter the height of the board: ')
    while not valid_int_over_zero(cols):
        cols = input('Enter the height of the board: ')
    cols = int(cols)
    filename = input('Enter the name of the file containing your ship placements: ')
    AI = input("Choose your AI.\n1. Random\n2. Smart\n3. Cheater\nYour choice:")
    while not num_between_1_and_3(AI):
        AI = input("Choose your AI.\n1. Random\n2. Smart\n3. Cheater\nYour choice:")
    AI = int(AI)
    dict_of_moves = ship_location_dictionary(filename, rows, cols)
    boat_symbol_size = symbol_and_size_dict(dict_of_moves)
    list_of_ships_already_placed = []
    list_of_userships = list_of_user_ships(dict_of_moves)
    #if dict_of_moves == {'P': [(0, 0)]}:
        #dictionary_of_symbols_and_coordinates = {'P': [(0, 0)]}
    #else:
    dictionary_of_symbols_and_coordinates = choses_AI_placement(list_of_ships_already_placed, boat_symbol_size, rows, cols)
    #print(dictionary_of_symbols_and_coordinates)
    list_of_AIships = list_of_AI_ships(dictionary_of_symbols_and_coordinates)
    for symbol, little_coord_list in dictionary_of_symbols_and_coordinates.items():
        start_coord = little_coord_list[0]
        end_coord = little_coord_list[-1]
        print('Placing ship from %d,%d to %d,%d.' % (start_coord[0], start_coord[1], end_coord[0], end_coord[1]))
    blank_char = "*"
    users_board = make_board(cols, rows, blank_char)
    ai_board = make_board(cols, rows, blank_char)
    scanning_board = make_board(cols, rows, blank_char)
    #placing ships on boards:
    users_board = user_board(dict_of_moves, users_board)
    ai_board = user_board(dictionary_of_symbols_and_coordinates, ai_board)

    print('ai board')
    display_game_state(ai_board)

    turn = random.randint(0,1)
    mode = 'hunt'
    already_sunk_by_user = []
    already_sunk_by_ai = []
    spot = []
    unfired = unfired_options(rows, cols)
    coords_to_fire_cheat = AI_coords_to_fire_cheat(dict_of_moves)
    while not ship_sunk_game_over(list_of_user_ships, scanning_board, users_board, dict_of_moves, ai_board, already_sunk_by_user, already_sunk_by_ai):
        # print('AI:')
        # display_game_state(ai_board)
        if turn == 0:
            print('Scanning Board')
            display_game_state(scanning_board)
            print()
            print("My Board")
            display_game_state(users_board)
            print()
            user_move = input('Enter row and column to fire on separated by a space: ')
            while not is_valid_move(user_move, ai_board):
                user_move = input('Enter row and column to fire on separated by a space: ')
            usermove = user_move.split()
            row_move = int(usermove[0])
            col_move = int(usermove[1])
            if ai_board[row_move][col_move] != '*':
                update_game_state("X", row_move, col_move, ai_board)
                update_game_state("X", row_move, col_move, scanning_board)
                if (not user_sinks_ai(ai_board, dict_of_moves, already_sunk_by_user)) and (not ai_sinks_user(users_board, dict_of_moves, already_sunk_by_ai)):
                    print('Hit!')
            else:
                update_game_state("O", row_move, col_move, ai_board)
                update_game_state("O", row_move, col_move, scanning_board)
                print('Miss!')
            turn = 1
        elif turn == 1:
            if AI == 1:
                random_AI_attack(unfired, users_board, ai_board, dict_of_moves, already_sunk_by_user, already_sunk_by_ai)
                turn = 0
            if AI == 2:
                if smart_AI_attack(spot, mode, unfired, users_board, rows, cols, dict_of_moves, ai_board, already_sunk_by_user, already_sunk_by_ai) == 'destroy':
                   smart_AI_attack(spot, 'destroy', unfired, users_board, rows, cols, dict_of_moves, ai_board,
                                    already_sunk_by_user, already_sunk_by_ai)
                else:
                    smart_AI_attack(spot, 'hunt', unfired, users_board, rows, cols, dict_of_moves, ai_board,
                                    already_sunk_by_user, already_sunk_by_ai)
                turn = 0
            if AI == 3:
                cheating_AI_attack(coords_to_fire_cheat, dict_of_moves, users_board, ai_board, already_sunk_by_user, already_sunk_by_ai)
                turn = 0

main()
