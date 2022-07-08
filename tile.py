class Tile():
	def __init__(self, value: int) -> None:
		#if type(x) is not int:
#			raise ValueError(f"x is {type(x)} not int")
#		if type(y) is not int:
#			raise ValueError(f"y is {type(y)} not int")
#		if type(value) is not int:
#			raise ValueError(f"value is {type(value)} not int")
#	
#		self.x = x
#		self.y = y
		self.value = value
		
	#def get_coords(self) -> tuple:
#		return self.x, self.y
#		
#	def set_coords(self, x: int, y: int):
#		if type(x) is not int:
#			raise ValueError(f"x is {type(x)} not int")
#		if type(y) is not int:
#			raise ValueError(f"y is {type(y)} not int")
#			
#		self.x = x
#		self.y = y
		
	def get_value(self):
		return self.value
		
	def set_value(self, val: int):
		if type(val) is not int:
			raise ValueError(f"val is {type(x)} not int")
			
		self.value = val
		
if __name__ == "__main__":
	t = Tile(0)
	print(t.get_value())
	t.set_value(1)
	print(t.get_value())