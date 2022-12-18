import string

class Board:
    def __init__(self):
        self.board = [[i + str(j) for i in string.ascii_lowercase[0:8]] for j in range(1, 9)]
        self.cell = dict([(i + str(j), 0) for i in string.ascii_lowercase[0:8] for j in range(1, 9)])

    def print_board(self):
        for i in range(8):
            string_print = []
            for pos in self.board[i]:
                if self.cell[pos] == 0:
                    string_print.append(pos + '(Empty)')
                elif self.cell[pos].color == "B":
                    string_print.append(pos + '(Black)')
                elif self.cell[pos].color == "W":
                    string_print.append(pos + '(White)')
            print(string_print)

    def initiative(self):
        for i in ["h8", "f8", "d8", "b8", "g7", "e7", "c7", "a7", "h6", "f6", "d6", "b6"]:
            self.cell[i] = Pieces(mother_board=self.cell, start_position=i, color='B')
        for i in ["a1", "c1", "e1", "g1", "b2", "d2", "f2", "h2", "a3", "c3", "e3", "g3"]:
            self.cell[i] = Pieces(mother_board=self.cell, start_position=i, color='W')

class Pieces:
    def __init__(self, mother_board, start_position, color):
        self.position = start_position
        self.alphabet = [i for i in string.ascii_lowercase[0:8]]
        self.beta = [j for j in range(1, 9)]
        self.color = color
        self.mother_board = mother_board

    def can_move(self):
        if self.alphabet.index(self.position[0]) == 0:
            move = [self.alphabet[self.alphabet.index(self.position[0]) + 1]]
            eat_move = [self.alphabet[self.alphabet.index(self.position[0]) + 1]]
        elif self.alphabet.index(self.position[0]) == 7:
            move = [self.alphabet[self.alphabet.index(self.position[0]) - 1]]
            eat_move = [self.alphabet[self.alphabet.index(self.position[0]) - 1]]
        elif self.alphabet.index(self.position[0]) == 6:
            move = [self.alphabet[self.alphabet.index(self.position[0]) - 1]]
            right_move = self.alphabet[self.alphabet.index(self.position[0]) + 1]
            left_move = self.alphabet[self.alphabet.index(self.position[0]) - 1]
            move = [right_move, left_move]
            eat_move = [right_move, left_move]
        elif self.alphabet.index(self.position[0]) == 1:
            move = [self.alphabet[self.alphabet.index(self.position[0]) - 1]]
            right_move = self.alphabet[self.alphabet.index(self.position[0]) + 1]
            left_move = self.alphabet[self.alphabet.index(self.position[0]) - 1]
            eat_right_move = self.alphabet[self.alphabet.index(self.position[0]) + 2]
            move = [right_move, left_move]
            eat_move = [eat_right_move, left_move]
        else:
            right_move = self.alphabet[self.alphabet.index(self.position[0]) + 1]
            left_move = self.alphabet[self.alphabet.index(self.position[0]) - 1]
            eat_right_move = self.alphabet[self.alphabet.index(self.position[0]) + 2]
            eat_left_move = self.alphabet[self.alphabet.index(self.position[0]) - 2]
            move = [right_move, left_move]
            eat_move = [eat_right_move, eat_left_move]
        if self.color == "W":
            for i in range(len(move)):
                if move[i] != eat_move[i]:
                    eat_move[i] += str(int(self.position[1]) + 2)
                    move[i] += str(int(self.position[1]) + 1)
                else:
                    eat_move[i] += str(int(self.position[1]) + 1)
                    move[i] += str(int(self.position[1]) + 1)
        if self.color == "B":
            for i in range(len(move)):
                if move[i] != eat_move[i]:
                    eat_move[i] += str(int(self.position[1]) - 2)
                    move[i] += str(int(self.position[1]) - 1)
                else:
                    eat_move[i] += str(int(self.position[1]) - 1)
                    move[i] += str(int(self.position[1]) - 1)
        for i in move[:]:
            if int(i[1]) > 8 or int(i[1]) < 1:
                move.remove(i)
                eat_move.remove(eat_move[move.index(i)])
        for i in move[:]:
            if 0 != self.mother_board[i] and self.mother_board[i].color == self.color:
                eat_move.remove(eat_move[move.index(i)])
                move.remove(i)
        new_move = []
        for i in move[:]:
            if 0 != self.mother_board[i] and self.mother_board[i].color != self.color and self.mother_board[
                eat_move[move.index(i)]] == 0:
                new_move.append(eat_move[move.index(i)])
                move.remove(i)
            elif 0 != self.mother_board[i]:
                move.remove(i)
        move += new_move
        return move

    def make_move(self, position_to):
        prev_pos = self.position
        if int(prev_pos[1])+2 == int(position_to[1]):
            self.mother_board[self.alphabet[self.alphabet.index(prev_pos[0]) + 1] + str(int(prev_pos[1]) + 1)] = 0
        if int(prev_pos[1])-2 == int(position_to[1]):
            self.mother_board[self.alphabet[self.alphabet.index(prev_pos[0]) - 1] + str(int(prev_pos[1]) - 1)] = 0
        self.mother_board[position_to] = self
        self.mother_board[position_to].position = position_to
        self.mother_board[prev_pos] = 0


game_board = Board()
game_board.initiative()

game = 0
while game == 0:
    for turn in ['W', "B"]:
        if turn == 'W':
            print("Ходят белые")
            check_can_move = [j for j,i in game_board.cell.items() if i != 0 and i.color == 'W' and i.can_move() != []]
            if check_can_move == []:
                game = 1
                break
        if turn == 'B':
            print("Ходят черные")
            check_can_move = [j for j,i in game_board.cell.items() if i != 0 and i.color == 'B' and i.can_move() != []]
            if check_can_move == []:
                game = 1
                break
        game_board.print_board()
        print('Доступные пешки ', check_can_move)
        checker = input("Введите пешку")
        while checker not in check_can_move:
            checker = input("Введите верную пешку")
        checker_can_move = game_board.cell[checker].can_move()
        print('Доступные ходы ', checker_can_move)
        checker_move = input("Введите ход")
        while checker_move not in checker_can_move:
            checker_move = input("Введите верный ход")
        game_board.cell[checker].make_move(checker_move)