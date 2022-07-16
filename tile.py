class Tile():
	def __init__(self, value: int) -> None:
		self.value = value
		self.rules = []
		self.entropy = 0
		self.dirs = []
		self.collapsed = False
		
	def get_value(self) -> int:
		return self.value
		
	def set_value(self, val: int) -> None:
		if type(val) is not int:
			raise ValueError(f"val is {type(x)} not int")
		if val != -1:
			self.collapsed = True
				
		self.value = val
		
	def add_rule(self, rule: tuple) -> None:
		self.rules.append(rule)
		
	def get_rules(self) -> list:
		return self.rules
		
	def set_entrpy(self, e: tuple) -> None:
		self.entropy = e
		
	def get_entropy(self) -> int:
		return self.entropy
		
	def add_dir(self, dir: tuple) -> None: # maybe extend only
		self.dirs.append(dir)
		
	def get_dirs(self) -> list:
		return self.dirs
		
	def set_col(self, val: bool) -> bool:
		self.collapsed = val
		
	def get_col(self) -> bool:
		return self.collapsed