class Board:
    def __init__(self, board_range=int()):
        self.board = [[' ' for i in range(board_range)] for i in range(board_range)]
        self.diag = board_range

    def print_board(self):
        for i in range(board_range):
            print(self.board[i])

    def new_xy(self, xy, coordinate_1, coordinate_2):
        self.board[coordinate_1][coordinate_2] = xy

    def its_final(self, xy):

        for i in range(self.diag):
            if self.board[i].count(xy) == self.diag:
                return True

        temp1 = []
        for i in range(self.diag):
            temp1.append(self.board[i][i])
        if temp1.count(xy) == self.diag:
            return True

        temp2 = []
        for i in range(self.diag):
            temp2.append(self.board[self.diag - 1 - i][i])
        if temp2.count(xy) == self.diag:
            return True

        for i in range(self.diag):
            temp3 = []
            for j in range(self.diag):
                temp3.append(self.board[j][i])
                if temp3.count(xy) == self.diag:
                    return True


n = input('Вы ходите использовать классическую доску 3? (y/n)')


def new_r():
    new_range = int(input('Введите размер достки (нечетное)'))
    if new_range % 2 != 1:
        print('число четное, введите еще раз')
        new_r()
    return new_range


range_default = 3

if n == 'n':
    range_default = new_r()

new_game = Board(board_range=range_default)
new_game.print_board()


def vvod():
    coor_1 = int(input('Введите строчку '))
    coor_2 = int(input('Введите столбец '))
    if new_game.board[coor_1 - 1][coor_2 - 1] != " ":
        print('ячейка уже занята')
        return vvod()
    else:
        return [coor_1, coor_2]


x = 0
while x == 0:
    for XY in ['X', 'Y']:
        print(f'Ходят {XY}')
        coor_1, coor_2 = vvod()
        new_game.new_xy(XY, coor_1 - 1, coor_2 - 1)
        new_game.print_board()
        if new_game.its_final(XY):
            print(f'Победили {XY}')
            x = 1
            break
