"""
    A Tic Tac Toe game script
    by: James R Brown
"""
import random

START_BOARD = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
X_PIECE = 'X'
O_PIECE = 'O'


class Player:
    def __init__(self, name=None, piece=None):
        self.name = name
        self.games_won = 0
        self.piece = piece

    def __repr__(self):
        return str(self.name)


class Game:
    def __init__(self, game_board=None, *players):
        self.winner = False
        self.game_board = game_board
        self.players = [x for x in players ]
        self.draws = 0

    def print_game_board(self):
        display = "____0___1___2___\n"
        for i, row in enumerate(self.game_board):
            n_row = f'{i} | {row[0]} | {row[1]} | {row[2]}'
            if i < 2:
                display += n_row + '\n'
                display += '  |---|---|---\n'
            else:
                display += f'{n_row}\n'

        return display

    def get_game_board(self):
        return self.game_board
    
    def set_game_board(self, new_board):
        for y in range(len(self.game_board)):
            for i in range(len(self.game_board[y])):
                self.game_board[y][i] = '-'


    def set_player_choice(self, choice, player):
        x = int(choice[0])
        y = int(choice[1])

        if player:
            if self.game_board[y][x] == '-':
                self.game_board[y][x] = player.piece
                return True

        return False

    def check_win(self):

        if self.check_rows():
            return True

        if self.check_cols():
            return True

        if self.check_diag():
            return True

        return False

    def check_rows(self):
        for row in self.game_board:
            row_str = "".join(row)
            if row_str == 'XXX' or row_str == 'OOO':
                return True

        return False

    def check_cols(self):
        col = 0
        col_value = ''
        while col < 3:
            for i in range(3):
                col_value += self.game_board[i][col]
            if col_value == 'XXX' or col_value == 'OOO':
                return True
            else:
                col += 1
                col_value = ''

        return False

    def check_diag(self):
        first_d = ''
        second_d = ''

        for i in range(3):
            first_d += self.game_board[i][i]
        if first_d == 'XXX' or first_d == 'OOO':
            return True

        second_d += self.game_board[0][2]
        second_d += self.game_board[1][1]
        second_d += self.game_board[2][0]

        if second_d == 'XXX' or second_d == 'OOO':
            return True

        return False

    def check_draw(self):
        t_count = 0
        for row in self.game_board:
            t_count += row.count('-')

        if t_count < 3:
            return True
        return False

    def print_instructuions(self):
        inst = """
                  Enter the coordinates you want to place your piece, I.E. - 00 OR 11
                  By default player one is 'X' and payer 2 is 'O'.
                  Each turn order is chosen randomly.. It is tic tac toe...
               """
        return inst


def flip_for_go(order):
    rand = random.randint(1,11)
    tmp = None
    if rand%2 != 0:
        tmp = order.pop()
        order.insert(0, tmp)

    return order


def main():
    welcome_screen = """
        **************************************************
        **************************************************
        *                                                *
        *                     Welcome                    *
        *                    Let's Play                  *
        *                    TIC TAC TOE                 *
        *                                                *
        **************************************************
        **************************************************
        """
    print(welcome_screen)
    # 1 player or 2 ?
    num_players = input('Number of players?: ')
    if num_players == '1':
        p1_name = input('Please enter players name: ')
        p2_name = 'comp_billy'
    elif num_players == '2':
    # get player names
        p1_name = input('Please enter a name for player 1: ')
        p2_name = input('Please enter a name for player 2: ')

    p1 = Player(name=p1_name, piece='X')
    p2 = Player(name=p2_name, piece='O')

    players = [p1,p2]
    game = Game(START_BOARD, players)

    keepgoing = True
    order = flip_for_go(players)

    while keepgoing:
        win = False
        # Print GameBoard
        keepgoing = False
        print(game.print_game_board())
        while not win:
            for player in order:
                selection = input(f'{player.name} enter you choice: ')
                if game.set_player_choice(selection, player):
                    print(game.print_game_board())
                    if game.check_win():
                        print(f'{player.name} Wins!')
                        player.games_won += 1
                        win = True
                        break

                    if game.check_draw():
                        game.draws += 1
                        print("Game Draw")
                        print(f'{game.draws} draws')
                        win = True
                        break

                else:
                    print('Sorry, occupied, try again!')
                    selection = input(f'{player.name} enter you choice: ')
                    if game.set_player_choice(selection, player):
                        print(game.print_game_board())
                        if game.check_win():
                            print(f'{player.name} Wins!')
                            player.games_won += 1
                            win = True
                            break
                        else:
                            if game.check_draw():
                                game.draws += 1
                                print("Game Draw")
                                print(f'{game.draws} draws')
                                win = True
                                break

        order = flip_for_go(order)
        game.set_game_board(START_BOARD)
        kg = input('Do you want to play another game?y/n: ')
        if kg == 'y' or kg == 'Y':
            keepgoing = True
        score=''
        score += f'{order[0].name} : {order[0].games_won} VS '
        score += f'{order[1].name} : {order[1].games_won}'
        print(score)
        win == False


if __name__ == '__main__':
    main()
