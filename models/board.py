from models.position import Position
from models.peca import Piece

class Board:
    def __init__(self, lines:int, columns:int):
        self.column = columns
        self.line = lines
        self.positions = [[Position(line, column) for column in range(columns)] for line in range(lines)]
        self.initials_position = []
        self.pieces = []
        self.initial_pieces_positions()

    def place_piece(self, line:int, column:int,team:int):
        position = self.positions[line][column]
        position.ocupada = True
        piece = Piece(line,column,team)
        self.pieces.append(piece)


    def search_position(self, line:int, column:int):
        for positions_row in self.positions:
            for position in positions_row:
                if position.line == line and position.column == column:
                    return position

        return None

    def initial_pieces_positions(self,):
        for positions_row in self.positions:
            for position in positions_row:
                if position.line == 2 and (2 <= position.column and position.column <= 5):
                    self.place_piece(position.line, position.column, 1)
                elif position.line == 9 and (2 <= position.column  and position.column <= 5):
                    self.place_piece(position.line, position.column, 2)
                elif position.column == 2:
                    if position.line < 2 or position.line > 9:
                        self.place_piece(position.line, position.column, 1)
                elif position.column == 5:
                    if position.line < 2 or position.line > 9:
                        self.place_piece(position.line, position.column, 2)

    def __str__(self) -> str:
        return f"Board(lines:{self.line}, columns:{self.column})"



