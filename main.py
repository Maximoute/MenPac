from Model import Board
from Model import Level
from Controller import BoardController

Niveau = Level.Level()
Plateau = Board.Board(Niveau.level_1)
ControllerPlateau = BoardController.BoardController(Plateau)
ControllerPlateau.printBoard()