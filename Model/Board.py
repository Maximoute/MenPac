from Model import Wall

class Board(object):
	"""docstring for ClassName"""
	def __init__(self,level):
		self.level = level 
		self.isInGame = False
		self.isGameOver = False
		self.matrix = self.initBoard()

	def initBoard(self):
		board = []
		for i in range(len(self.level)):
			row = []
			for j in range(len(self.level[1])):
				# column = []
				if i == 0 or i == len(self.level) - 1 or j == 0 or j == len(self.level) - 1:
					row.append(Wall.Wall("Wall", 0))
				else:
					row.append(None)
			board.append(row)
		return board
