import pygame

class Cell: 
	def __init__(self, live, xcor, ycor, width, height):
		self.alive = live
		self.xcor = xcor
		self.ycor = ycor
		self.cell = pygame.Rect(xcor, ycor, width, height)
		self.neighbors = 0

	def get_cell(self):
		return self.cell

	def get_x(self):
		return self.xcor

	def get_y(self):
		return self.ycor

	def get_alive(self):
		return self.alive

	def get_neighbors(self):
		return self.neighbors

	def add_to_neighbors(self):
		self.neighbors += 1

	def breed(self):
		self.alive = self.neighbors == 3 or self.alive and self.neighbors == 2
		self.neighbors = 0

	def render_cell(self, screen):
		pygame.draw.rect(screen, (255, 255, 255), self.get_cell(), not self.get_alive())