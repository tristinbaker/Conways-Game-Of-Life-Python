import pygame, sys
from cell import Cell
from glider import glider
from copperhead import copperhead

pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 60

WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Game of Pyfe")
SCREEN = pygame.display.get_surface()

cells = []

cells = [[Cell(bool(live), x*20, y*20, WIDTH / 30, HEIGHT / 30) for x, live in enumerate(row)]
			for y, row in enumerate(glider)]

def check_neighbors():
	for i in range(30):
		for j in range(30):
			if i == 0 and j == 0:
				if cells[i][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j+1].get_alive():
					cells[i][j].add_to_neighbors()
			elif i == 0 and j == 29:
				if cells[i][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j].get_alive():
					cells[i][j].add_to_neighbors()
			elif i == 29 and j == 0:
				if cells[i-1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i][j+1].get_alive():
					cells[i][j].add_to_neighbors()
			elif i == 29 and j == 29:
				if cells[i][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j].get_alive():
					cells[i][j].add_to_neighbors()
			elif i == 0:
				if cells[i][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+j][j+1].get_alive():
					cells[i][j].add_to_neighbors()
			elif j == 0:
				if cells[i-1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j+1].get_alive():
					cells[i][j].add_to_neighbors()
			elif i == 29:
				if cells[i][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i][j+1].get_alive():
					cells[i][j].add_to_neighbors()
			elif j == 29:
				if cells[i-1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j].get_alive():
					cells[i][j].add_to_neighbors()
			else:
				if cells[i-1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i-1][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i][j+1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j-1].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j].get_alive():
					cells[i][j].add_to_neighbors()
				if cells[i+1][j+1].get_alive():
					cells[i][j].add_to_neighbors()

while True:
	SCREEN.fill((0, 0, 0))
	check_neighbors()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()	
			sys.exit()
	for i in range(30):
		for j in range(30):
			cells[i][j].render_cell(SCREEN)
			cells[i][j].breed()

	pygame.time.delay(200)

	pygame.display.flip()