class BoardController(object):
	"""docstring for ClassName"""
	def __init__(self, Board):
		self.Board = Board
		

	def printBoard(self):
		for lign in self.Board.matrix:
			for cell in lign:
				if cell is not None:
					if cell.name == "Wall":
						print("Wall", end=" ")
				else:
					print("XXXX", end=" ")
			print()