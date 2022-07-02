import os, pygame

# os.system("cls")

MAP_WIDTH, MAP_HEIGHT = 11, 11
MAP = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

WIDTH, HEIGHT = 64 * MAP_WIDTH, 64 * MAP_HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WFC")
FPS = 60

TILE_0 = pygame.image.load(os.path.join('Assets', 'red.png'))
TILE_1 = pygame.image.load(os.path.join('Assets', 'green.png'))
TILE_2 = pygame.image.load(os.path.join('Assets', 'blue.png'))

def main():
	clock = pygame.time.Clock()
	run = True
	wfc()
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		draw_window()

def draw_window():
	WIN.fill((0, 0, 0))

	for i, row in enumerate(MAP):
		for j, _ in enumerate(row):
			if MAP[i][j] == 1:
				WIN.blit(TILE_0, (64 * i, 64 * j))
			if MAP[i][j] == 2:
				WIN.blit(TILE_1, (64 * i, 64 * j))
			if MAP[i][j] == 3:
				WIN.blit(TILE_2, (64 * i, 64 * j))

	pygame.display.update()

def wfc():
	MAP[5][5] = 1

	for i in range(5):
		MAP[5][i] = 1
		MAP[i][5] = 1
		MAP[5][i+6] = 1
		MAP[i+6][5] = 1
		
		MAP[0][i] = 1
		MAP[i+6][0] = 1
		MAP[i][10] = 1
		MAP[10][i+6] = 1

if __name__ == "__main__":
	main()