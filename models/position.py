class Position():
    def __init__(self,line,column,ocupada=False):
        self.line = line
        self.column = column
        self.__ocupada = ocupada
    
    @property
    def line(self):
        return self.__line
    
    @line.setter
    def line(self, newLine:int):
        self.__line = newLine

    @property
    def column(self,):
        return self.__column
    
    @column.setter
    def column(self,newColumn:int):
        self.__column = newColumn

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self,newOcupada:bool):
        self.__ocupada = newOcupada

    def __str__(self):
        return f"Position: (line={self.__line}, column={self.__column}, ocupada={self.__ocupada})"

