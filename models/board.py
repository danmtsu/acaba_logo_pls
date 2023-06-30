from models.position import Position
from models.peca import Piece

class Board:
    def __init__(self, lines:int, columns:int):
        self.column = columns
        self.line = lines
        self.positions = [[Position(line, column) for column in range(columns)] for line in range(lines)]

    def place_piece(self, line:int, column:int,team:int):
        position = self.positions[line][column]
        position.ocupada = True
        Piece(line,column,team)

    def search_position(self, line:int, column:int):
        for positions_row in self.positions:
            for position in positions_row:
                if position.line == line and position.column == column:
                    return position
    
        return None
    
    
    def __str__(self) -> str:
        return f"Board(lines:{self.line}, columns:{self.column})"



