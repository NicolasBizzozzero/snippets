from enum import IntEnum
from typing import List


class Representation(IntEnum):
	ADJACENCE_MATRIX = 0
	ADJACENCE_LIST = 1


class Vertex():
	"""
	Attributes:
		label: string
	"""
	def __init__(self, label: str):
		self.label = label

	def __equals__(self, other):
		return self.label == other.label

	def degree(self) -> int:
		pass


class Edge():
	"""
	
	Attributes:
		start_vertex: Vertex
		end_vertex: Vertex
		weight: int
	"""
	def __init__(self, start_vertex: Vertex, end_vertex: Vertex,
		         weight: int = 1):
		self.start_vertex = start_vertex
		self.end_vertex = end_vertex
		self.weight = weight


class Graph():
	def __init__(self, representation: Representation, directed=True):
		if representation == Representation.ADJACENCE_MATRIX:
			pass
		elif representation == Representation.ADJACENCE_LIST:
			pass
		else:
			raise UnknownRepresentation(representation)
