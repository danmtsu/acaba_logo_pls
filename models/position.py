class Position():
    def __init__(self, line, column, ocupada=False,):
        self.__line = line
        self.__column = column
        self.__ocupada = ocupada
        
    @property
    def line(self):
        return self.__line
    
    @line.setter
    def line(self, newLine):
        self.__line = newLine

    @property
    def column(self):
        return self.__column
    
    @column.setter
    def column(self, newColumn):
        self.__column = newColumn

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, newOcupada):
        self.__ocupada = newOcupada

    def __str__(self) -> str:
        return f"Position: (line={self.line}, column={self.column}, ocupada={self.ocupada})"
