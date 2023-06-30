from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from models.board import Board
import os

class PlayerInterface():
    def __init__(self):# construção da interface e interface do tabuleiro na chamada do objeto PlayerInterface
        self.main_window = Tk() # instanciar Tk (que implementa a janela)
        #  preenchimento da janela
        self.fill_main_window()# chamada da função fill_main_window para o tratamento da interface inicial do player
        self.main_window.mainloop() # abrir a janela
        self.board = None


    def fill_main_window(self):
        self.main_window.title('PiqueBandeira')
        self.main_window.geometry('1280x720')
        self.main_window.resizable(False, False)
        self.main_window["bg"]="gold3"

        #Criação de dois frames e organização da janela em um gridde 2 linhas e uma coluna,
        #sendo que a table_frame ocupa a linha superior e a message_frame a inferior
        self.table_frame = Frame(self.main_window, padx=15, pady=15,bg='gold3')
        self.table_frame.grid(row=0,column=0)
        self.message_frame = Frame(self.main_window, padx=0, pady=10,bg='gold3')
        self.message_frame.grid(row=1,column=0)


        # Criação de um menu para o programa
        # Criar a barra de menu (menubar) e adicionar à janela:
        self.menubar = Menu(self.main_window)
        self.menubar.option_add("*tearOff", FALSE)
        self.main_window["menu"] = self.menubar
        # Adicionar menu(s) à barra de menu:
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label="File")
        # Adicionar itens de menu a cada menu adicionado à barra de menu:
        self.menu_file.add_command(label="Iniciar jogo", command=print('Jogo iniciado'))
        self.menu_file.add_command(label="Restaurar estado inicial",command=print('jogo resetado'))

        self.an_image = PhotoImage(file="./images/yellow_square.png")
        self.other_image = PhotoImage(file="./images/rectangle.png")
        self.oponnent_image = PhotoImage(file="./images/enemy_rectangle.png")
# Preenchimento de table_frame com 21 imagens iguais, organizadas em 3 linhas e 7 colunas
        self.board_view=[]
        self.initialize_board(8,12)
        for y in range(8):
            a_column = [] # columns
            for x in range(12):
                if x < 6:
                    aLabel = Label(self.table_frame, bd = 0, image=self.other_image)
                else:
                    aLabel = Label(self.table_frame, bd = 0, image=self.oponnent_image)
                aLabel.bind("<Button-1>", lambda event, a_line=x, a_column=y: self.click(event, a_line, a_column))
                aLabel.grid(row=x , column=y)
                a_column.append(aLabel)
            self.board_view.append(a_column)

    
    def initialize_board(self,line,column):
        self.board = Board(line,column)




    def click(self, event,line,column):
        print(self.board.search_position(line,column))
        print('CLICK',line,column)
