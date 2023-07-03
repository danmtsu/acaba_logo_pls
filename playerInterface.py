from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Canvas
from PIL import ImageTk, Image
from models.board import Board
import os

class PlayerInterface():
    def __init__(self):
        self.main_window = Tk()
        self.fill_main_window()
        self.main_window.mainloop()
        self.board = None
        self.images_pieces1 = []
        self.images_pieces2 = []
        self.piece_images = []
        self.piece_labels = {}  # Dicionário para armazenar os objetos Label das peças
        self.piece_images = []  # Lista para armazenar as imagens das peças
        self.last_clicked_label = None  # Última peça clicada



    def fill_main_window(self):
        self.main_window.title('PiqueBandeira')
        self.main_window.geometry('1280x720')
        self.main_window.resizable(False, False)
        self.main_window["bg"] = "gold3"

        self.table_frame = Frame(self.main_window, padx=15, pady=15, bg='gold3')
        self.table_frame.grid(row=0, column=0)
        self.message_frame = Frame(self.main_window, padx=0, pady=10, bg='gold3')
        self.message_frame.grid(row=1, column=0)

        self.menubar = Menu(self.main_window)
        self.menubar.option_add("*tearOff", FALSE)
        self.main_window["menu"] = self.menubar

        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label="File")
        self.menu_file.add_command(label="Iniciar jogo", command=print('Jogo iniciado'))
        self.menu_file.add_command(label="Restaurar estado inicial", command=print('jogo resetado'))

        self.an_image = PhotoImage(file="./images/yellow_square.png")
        self.other_image = PhotoImage(file="./images/rectangle.png")
        self.oponnent_image = PhotoImage(file="./images/enemy_rectangle.png")

        self.board_view = []
        self.initialize_board(12, 8)
        for y in range(8):
            a_column = []
            for x in range(12):
                if x < 6:
                    aLabel = Label(self.table_frame, bd=0, image=self.other_image)
                else:
                    aLabel = Label(self.table_frame, bd=0, image=self.oponnent_image)
                aLabel.bind("<Button-1>", lambda event, a_line=x, a_column=y: self.click(event, a_line, a_column))
                aLabel.grid(row=x, column=y)
                a_column.append(aLabel)
            self.board_view.append(a_column)
            print([position for position in self.board.positions])
            print([(piece.line, piece.column) for piece in self.board.pieces])
        self.load_piece_images()
        self.draw_initial_pieces()

    def initialize_board(self, line, column):
        self.board = Board(line, column)

    def draw_initial_pieces(self):
        raio = 15
        self.piece_buttons = {}  # Dicionário para armazenar os botões das peças

        for piece in self.board.pieces:
            x = piece.column * 50 + 25
            y = piece.line * 50 + 25

            if piece.team == 1:
                piece_image = Image.open("./images/piece_team1.png").convert("RGBA")
                piece_image = piece_image.resize((2 * raio, 2 * raio), Image.BICUBIC)
                piece_image = ImageTk.PhotoImage(piece_image)

                piece_button = Button(self.table_frame, image=piece_image, bd=0, highlightthickness=0)
                piece_button.image = piece_image
                piece_button.place(x=x, y=y, anchor='center')

                self.piece_buttons[piece] = piece_button

            elif piece.team == 2:
                piece_image = Image.open("./images/piece_team2.png").convert("RGBA")
                piece_image = piece_image.resize((2 * raio, 2 * raio), Image.BICUBIC)
                piece_image = ImageTk.PhotoImage(piece_image)

                piece_button = Button(self.table_frame, image=piece_image, bd=0, highlightthickness=0)
                piece_button.image = piece_image
                piece_button.place(x=x, y=y, anchor='center')

                self.piece_buttons[piece] = piece_button

                piece_button.config(command=lambda btn=piece_button: self.click(btn, piece))


    def load_piece_images(self):
        self.piece_images = []  # Limpar a lista de imagens das peças

        for file in os.listdir("./images"):
            if file.endswith(".png"):
                image = Image.open(os.path.join("./images", file)).convert("RGBA")
                self.piece_images.append(image)


    def click(self, button, piece):
        # Alterar o estilo do botão quando clicado
        button.config(bg="green") # Limpar o fundo das outras peças
