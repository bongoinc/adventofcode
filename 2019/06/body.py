class Body:
	def __init__(self, p=None):
		self.parent = p
		self.children = []
	
	def addChild(self, c):
		self.children.append(c)
		
	@property
	def numChildren(self):
		return len(self.children)
