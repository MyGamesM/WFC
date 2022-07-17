import pygame
from tile import Tile
from map import Map

class game:
	def __init__(self) -> None:
		self.map = Map(4, 4)
		self.width, self.height = 64 * self.map.get_size()[0], 64 * self.map.get_size()[1]
		self.window = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("WFC")
		
		self.fps = 60
		self.clock = pygame.time.Clock()
		self.run = True
		self.tiles = []
		
		self.load_assets()
		self.wfc()
		self.calculate_entropy()
		self.tick()

	def load_assets(self) -> None:
		tiles = os.listdir(f"{os.getcwd()}//Assets")
		tiles.sort()
		for tile in tiles:
			self.tiles.append(pygame.image.load(os.path.join('Assets', tile)))
						
	def tick(self) -> None:
		while self.run:
			self.clock.tick(self.fps)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
					
			self.draw_window()
					
		pygame.quit()
					
	def draw_window(self) -> None:
		self.window.fill((0, 0, 0))

		for i, column in enumerate(self.map.get()):
			for j, tile in enumerate(column):
				for k in range(len(self.tiles)):
					if tile.get_col() and tile.get_value() == k:
						self.window.blit(self.tiles[k], (64 * j, 64 * i))
						
		pygame.display.update()

	def wfc(self) -> None:
		for i, column in enumerate(self.map.get()):
			for j, tile in enumerate(column):
				self.map.set_tile(j, i, Tile(-1), False)

		self.map.set_tile(1, 0, Tile(2), True)
		self.map.get_tile(1, 0).add_rule((0, (2, 3, 4)))
		self.map.get_tile(1, 0).add_rule((1, (1, 3, 4)))
		self.map.get_tile(1, 0).add_rule((2, (0, 4)))
		self.map.get_tile(1, 0).add_rule((3, (1, 2, 3)))
		self.map.get_tile(1, 0).set_col(True)

	def directions(self) -> None:
		max_y, max_x = self.map.get_size()
		for i, column in enumerate(self.map.get()):
			for j, tile in enumerate(column):
				tile = self.map.get_tile(j, i)
				dirs = []

				x, y = j, i

				if x == 0:
					dirs.append(1)
				elif x == max_x:
					dirs.append(3)
				else:
					dirs.extend([1, 3])

				if y == 0:
					dirs.append(2)
				elif y == max_y:
					dirs.append(0)
				else:
					dirs.extend([0, 2])

				dirs.sort()
				
				for k in range(len(dirs)):
					if k == 0:
						continue
						
					if dirs[k] == dirs[k-1]:
						dirs.pop(i)

				if x != 0 or x != max_x:
					if y > 0:
						if self.map.get_tile(x, y-1).get_value() != -1:
							dirs.remove(0)

					if y != max_y:
						if self.map.get_tile(x, y+1).get_value() != -1:
							dirs.remove(2)

				if y != 0 or y != max_y:
					if x > 0:
						if self.map.get_tile(x-1, y).get_value() != -1:
							dirs.remove(3)

					if x != max_x:
						if self.map.get_tile(x+1, y).get_value() != -1:
							dirs.remove(1)

				for dir in dirs:
					tile.add_dir(dir)

	def calculate_entropy(self) -> None:
		# print(self.map.get_tile(x, y).get_rules())

		for i, column in enumerate(self.map.get()):
			for j, tile in enumerate(column):
				if tile.get_col() is False:
					print(tile.get_dirs())
					# TODO: calculate the entropy of this tile based on its surrounding tiles

#								# (1 / len(dirs[k]) + math.log((1 / len(dirs[k]), 2)))

if __name__ == "__main__":
	from pprint import pp
	app = game()
	pp(app.map.get())