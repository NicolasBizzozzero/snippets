pi = 3.141592653589793

def factorial(x):
	total = 1
	for n in range(1, x+1):
		total *= n
	return total


def cos(x):
	# Congruence de l'angle x modulo 2*pi
	angle = x % (2*pi)

	# Angles remarquables (ameliore l'approximation)
	if angle == 0:
		return 1
	elif angle == pi/2:
		return 0
	elif angle == pi:
		return -1
	elif angle == (3*pi)/2:
		return 0

	# Inversion du signe si l'angle est superieur à pi
	if pi < angle:
		angle = -angle

	# Calcul à l'aide du développement limité de cos(x)
	somme = 0
	for n in range(16):
		somme += (((-1)**n)/factorial(2*n))*(angle**(2*n))
	return somme


def sin(x):
	# Congruence de l'angle x modulo 2*pi
	angle = x % (2*pi)

	# Angles remarquables (ameliore l'approximation)
	if angle == 0:
		return 0
	elif angle == pi/2:
		return 1
	elif angle == pi:
		return 0
	elif angle == (3*pi)/2:
		return -1

	# Inversion du signe si l'angle est superieur à pi
	if pi/2 < angle < (3*pi)/2:
		angle = -angle

	# Calcul à l'aide du développement limité de cos(x)
	somme = 0
	for n in range(16):
		somme += (((-1)**n)/factorial(2*n+1))*(angle**(2*n+1))
	return somme


def tan(x):
	if (x % 2*pi) == ((pi/2) or ((3*pi)/2)):
		raise ValueError
	return sin(x)/cos(x)


def exp(x):
	if x == 0:
		return 1
	somme = 0
	for n in range((x+15)*2):
		somme += (x**n)/(factorial(n))
	return somme


def ln(x):
	"""Retourne la valeur du logarithme néperien de x."""
	if x <= 0:
		raise ValueError
	if x == 1:
		return 0
	total = 0
	for n in range((x+15)*2):
		total += (((x-1)/(x+1))**((2*n)+1))/((2*n)+1)
	return 2*total


def log(x, a):
	"""Retourne la valeur du logarithme en base a de x."""
	if a == 1:
		raise ValueError
	return ln(x)/ln(a)


class Vector:
	"""n dimensional vector."""
	def __init__(self, *coordinates):
		"""Coordinates of self are stocked in a list."""
		self.dimension = 0
		self.coordinates = list()
		for elem in coordinates:
			self.dimension += 1
			self.coordinates.append(elem)


	def __str__(self):
		return str(self.coordinates)



class Polygon:
	"""n dimensional polygon."""
	def __init__(self, *vectors):
		"""Coordinates of self are same dimensional vectors stocked in a list."""
		if not are_in_the_same_dimension(vectors):
			return "The vectors taken has input are not same dimensional."
			# Raise ValueError:
		self.vectors = vectors
		self.dimension = vectors[0].dimension
		self.lenght = len(vectors)


	def are_in_the_same_dimension(vectors):
		"""return True if the dimension of all the vectors is the same, or False if not."""
		for i in range(len(vectors)-1):
			if vectors[i].dimension != vectors[i+1].dimension:
				return False
		return True


class Cercle:
	pass



point1 = Vector(4, 8, 15, 16, 23, 42)
point2 = Vector(4, 8, 15, 16, 23, 43)
polygone1 = Polygon(point1, point2)