import tkinter as tk
board_size_x = 10
board_size_y = 10

player = 2
wall = 1
void = 0

res = 50
def initBoard(x,y,wall,void):
	board = []
	for i in range(x):
		row = []
		for j in range(y):
			# column = []
			if i == 0 or i == x - 1 or j == 0 or j == x - 1:
				row.append(wall)
			else:
				row.append(void)
			# row.append(column)
		board.append(row)
	return board

def printBoard(board):
	for i in range(len(board)):

		print(board[i])

def createGrid(window,board,res,wall):
	for i in range(len(board)):
		for j in range(len(board[i])):
			x1 = j * res
			y1 = i * res
			x2 = x1 + res
			y2 = y1 + res
			if board[i][j] == wall:
				window.create_rectangle(x1,y1,x2,y2,outline="black",fill="blue")
			else:
				window.create_rectangle(x1,y1,x2,y2,outline="black",fill="white")

def createPlayer(window,board,res):
	for i in range(len(board)):
		for j in range(len(board[i])):
			x1 = j * res +(res/10)
			y1 = i * res +(res/10)
			x2 = (j+1) * res -(res/10)
			y2 = (i+1) *res -(res/10)
			if board[i][j] == player:
					window.create_oval(x1,y1,x2,y2,outline="black",fill="yellow")

board = initBoard(board_size_x,board_size_y,wall,void)
board[2][2] = player
root = tk.Tk()
window = tk.Canvas(root,width=board_size_x * res,height=board_size_y * res)
window.pack()
createGrid(window,board,res,wall)
createPlayer(window,board,res)
root.mainloop()