import numpy as np 
import pygame
import math

class Board():
	def __init__(self, row, column):
		self.Board = np.zeros((row,column))
		self.row = row
		self.col = column

	def draw(self, sizePawn):	
		for i in range(self.col):
			for j in range(self.row):
				pygame.draw.rect(screen, Gray, (i*sizePawn, j*sizePawn+sizePawn, sizePawn, sizePawn))
				pygame.draw.circle(screen, Black, (int(i*sizePawn+sizePawn/2), int(j*sizePawn+sizePawn+sizePawn/2)), int(sizePawn/2 - 5))
		
		for i in range(self.col):
			for j in range(self.row):		
				if self.Board[j][i] == 1:
					pygame.draw.circle(screen, Purple, (int(i*sizePawn+sizePawn/2), height-int(j*sizePawn+sizePawn/2)), int(sizePawn/2 - 5))
				elif self.Board[j][i] == 2: 
					pygame.draw.circle(screen, Green, (int(i*sizePawn+sizePawn/2), height-int(j*sizePawn+sizePawn/2)), int(sizePawn/2 - 5))
		pygame.display.update()

	def getRow(self, col):
		for i in range(self.row):
			if self.Board[i][col] == 0:
				return i
	def putPawn(self, row, col, player):
		self.Board[row][col] = player

	def validPlace(self, col):
		if(self.Board[self.row-1][col] == 0):
			return True
		else:
			return False

	def isWon(self, player):
		#horizontal
		for i in range(self.col-3):
			for j in range(self.row):
				if self.Board[j][i] == player and self.Board[j][i+1] == player and self.Board[j][i+2] == player and self.Board[j][i+3] == player:
					return True

		# Vertical
		for i in range(self.col):
			for j in range(self.row-3):
				if self.Board[j][i] == player and self.Board[j+1][i] == player and self.Board[j+2][i] == player and self.Board[j+3][i] == player:
					return True

		# Diag haut
		for i in range(self.col-3):
			for j in range(self.row-3):
				if self.Board[j][i] == player and self.Board[j+1][i+1] == player and self.Board[j+2][i+2] == player and self.Board[j+3][i+3] == player:
					return True

		# Diag Bas
		for i in range(self.col-3):
			for j in range(3, self.row):
				if self.Board[j][i] == player and self.Board[j-1][i+1] == player and self.Board[j-2][i+2] == player and self.Board[j-3][i+3] == player:
					return True

pygame.init()
police = pygame.font.SysFont("comicsansms", 30)
Gray = (120,120,120)
Black = (0,0,0)
Purple = (139,31,255)
Green = (21,214,86)
number_row = 6
number_col = 7
BOARD = Board(number_row, number_col)
finiched = False
turn = 0

sizePawn = 70

width = number_col * sizePawn
height = (number_row+1) * sizePawn
size = (width, height)

screen = pygame.display.set_mode(size)
BOARD.draw(sizePawn)
pygame.display.update()


while not finiched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, Black, (0,0, width, sizePawn))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, Purple, (posx, int(sizePawn/2)), int(sizePawn/2 - 5))
			else: 
				pygame.draw.circle(screen, Green, (posx, int(sizePawn/2)), int(sizePawn/2 - 5))
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/sizePawn))

				if BOARD.validPlace(col):
					row = BOARD.getRow(col)
					BOARD.putPawn(row, col, 1)

					if BOARD.isWon(1):
						label = police.render("J1 Wins !", 1, Purple)
						screen.blit(label, (40,10))
						finiched = True

			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/sizePawn))

				if BOARD.validPlace(col):
					row = BOARD.getRow(col)
					BOARD.putPawn(row, col, 2)

					if BOARD.isWon(2):
						label = police.render("J2 Wins !", 1, Green)
						screen.blit(label, (40,10))
						finiched = True

			BOARD.draw(sizePawn)

			turn += 1
			turn = turn % 2

			if finiched:
				pygame.time.wait(3000)
