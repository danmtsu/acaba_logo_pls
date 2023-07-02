class Piece():
    def __init__(self,line,column,team:int):
        self.__line = line
        self.__column = column
        self.__frozen = False
        self.__team = team
        self.__hasFlag = False

    @property
    def line(self,):
        return self.__line
    
    @property
    def column(self,):
        return self.__column
    
    @property
    def frozen(self,):
        return self.__frozen
    
    @line.setter
    def line(self,newLine:int):
        self.__line = newLine

    @column.setter
    def column(self,newColumn:int):
        self.__column = newColumn

    @frozen.setter
    def frozen(self,isFrozen:bool):
        self.__frozen = isFrozen

    @property
    def team(self,):
        return self.__team
    
    def cat_flag(self,):
        self.__hasFlag = True