# PyStockChess

PyStockChess is a program made in Python with Stockfish.

It has a variable depth and does not support castling due to a limitation of the wrapper used to use Stockfish.
( The wrapper takes moves by using a list of all moves taken, and does not respond properly if fed O-O-O or O-O. )

It has 2 dependencies:
* Pygame
* Pystockfish (wrapper for stockfish)
