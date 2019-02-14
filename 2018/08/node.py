class Node:
    def __init__(self):
        self._children = []
        self._metadata = []

    def add_child(self, node):
        self._children.append(node)

    def add_metadata(self, metadata):
        self._metadata.append(metadata)
