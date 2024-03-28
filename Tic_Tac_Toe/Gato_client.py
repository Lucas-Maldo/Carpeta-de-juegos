import socket
import threading

import pygame as pg
import sys
from pygame.locals import *


#create a client-server interaction where the client send a number indicating the position of his piece and the server returns a 
#9 or 5 digits if its the board or the winning coords and the message
#maybe I dont need threads for this Ill have to check without first

WIN_SIZE = 900
CELL_SIZE = WIN_SIZE // 3
CELL_CENTER = CELL_SIZE//2
board_path = "C:\Lucas things\Projects\Games\Carpeta-de-juegos\Tic_Tac_Toe\\board_tic_tac.png"
x_path = "C:\Lucas things\Projects\Games\Carpeta-de-juegos\Tic_Tac_Toe\X_tic_tac.png"
o_path = "C:\Lucas things\Projects\Games\Carpeta-de-juegos\Tic_Tac_Toe\O_tic_tac.png"
HOST = "192.168.0.14"
PORT = 12345


def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("You are player", data)
        message = b"Symbol recieved"
        client_socket.sendall(message)
        return client_socket, data

class Client_Game():
    def __init__(self, client_socket, symbol):
        pg.init()
        self.board = pg.transform.smoothscale(pg.image.load(board_path), [WIN_SIZE] *2)
        self.X_image = pg.transform.smoothscale(pg.image.load(x_path), [CELL_SIZE] *2)
        self.O_image = pg.transform.smoothscale(pg.image.load(o_path), [CELL_SIZE] *2)
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.screen.blit(self.board, (0,0))
        self.clock = pg.time.Clock()
        pg.display.set_caption( 'TIC TAC TOE' )
        self.font = pg.font.SysFont('Verdana', CELL_SIZE // 4, True)
        self.font2 = pg.font.SysFont('Verdana', CELL_SIZE // 10, True)
        self.client_socket = client_socket
        self.win_coords = []
        self.board = None
        self.current_player = symbol

    def display(self): #The board argument is the board recieved by the server
        for x, row in enumerate(self.board):
            for y, item in enumerate(row):
                if (item != "N" and self.win_coords == []):
                    self.screen.blit(self.X_image if (item == "X") else self.O_image, (y * CELL_SIZE, x * CELL_SIZE))
        pg.display.update()

    def check_events(self): #This funciton can only be used if the client has reciever the board and it has to be modified to send the index
        #first receive board as input and then the player can play one square
        while True:
            data = self.client_socket.recv(1024).decode()
            if not data:
                break
            self.board = [x.split(",") for x in data.split("/")]
            print(self.board)
            message = b"Board recieved"
            self.client_socket.sendall(message)
            self.display()

        for event in pg.event.get():
            if(event.type == MOUSEBUTTONDOWN and self.win_coords == []):
                y,x = event.pos
                y,x = y//CELL_SIZE ,x//CELL_SIZE
                if(self.board[x][y] == "N"): #There is no longer a current player, here it waits to recieve the baord from the server
                    self.board[x][y] = self.current_player #This means the server asigns a symbols for each player maybe randomly
                    coordinate = x * len(self.board) + y
                    self.client_socket.sendall(coordinate.encode())
            if(event.type == KEYDOWN): #This has to be changed into an offering to the other player in case he also wants to play again
                if(event.key == pg.K_SPACE):
                    self.__init__()
            if event.type == QUIT: #In case of quit the other player automatically wins
                pg.quit()
                sys.exit()

    def draw_win(self, message):
        if(self.win_coords != []):
            win_coords = [[i * CELL_SIZE + CELL_CENTER for i in item] for item in self.win_coords]
            # print(self.win_coords)
            pg.draw.line(self.screen, 'red', *win_coords, CELL_SIZE // 8)
            label = self.font.render(message, True, 'white', 'black')
            self.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 3))
            label = self.font2.render("(Space to rematch)", True, 'white', 'black')
            self.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 2))
            pg.display.update()

    def check_finish(board):
        if(len(board) == 1):
            return board #This will return the problem and let him play again
        if(len(board) == 5):
            return board #This will return the winning coordinates

    def play(self):

        while True:
            self.check_events()
            break
            self.display()
            message = self.check_finish()
            if(message):
                self.draw_win(message)
                # break

client_socket, symbol = connect_to_server(HOST, PORT)
game = Client_Game(client_socket, symbol)
game.play()


# def receive_messages(client_socket):
#     while True:
#         data = client_socket.recv(1024)
#         if not data:
#             break
#         print("Received from server:", data.decode())

# def main():
    
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((host, port))
    
#     # Start a thread to receive messages from the server
#     receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
#     receive_thread.start()
    
#     # Send messages to the server
#     try:
#         while True:
#             message = input("Enter message to send: ")
#             client_socket.sendall(message.encode())
#     except KeyboardInterrupt:
#         print("Caught keyboard interrupt, exiting")
#         client_socket.close()

        

# if __name__ == "__main__":
#     main()
