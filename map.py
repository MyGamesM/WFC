from tile import Tile

class Map:
	def __init__(self, width, height) -> None:
		self.map_width = width
		self.map_height = height
		self.generate_map()
		
	def generate_map(self) -> None:
		self.map = [[None for _ in range(self.map_width)] for _ in range(self.map_height)]

	def get(self) -> list:
		return self.map
	
	def get_size(self) -> tuple:
		return self.map_width - 1, self.map_height - 1
		
	def get_tile(self, x: int, y: int) -> Tile or None:
		return self.map[y][x]
		
	def set_tile(self, x: int, y: int, tile: Tile, override: bool):
		if self.map[y][x] is None or override is True:
			self.map[y][x] = tile