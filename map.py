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
		return self.map_width, self.map_height
		
	def get_tile(self, x: int, y: int) -> Tile or None:
		return self.map[y][x]
		
	def set_tile(self, x: int, y: int, tile: Tile, override: bool):
		if self.map[y][x] is not None or override is True:
			self.map[y][x] = tile
	
if __name__ == "__main__":
	from pprint import pp
	
	map = Map(4, 4)
	map.set_tile(1, 2, Tile(0, 0, 0), True)
	
	pp(map.get())
	print("---")
	print(map.get_tile(1, 2))
	print("---")
	print(map.get_tile(1, 2).get_coords())