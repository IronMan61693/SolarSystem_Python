#!/usr/bin/env python3

# Homework Assignment 2+
# Requirements: Create a planet class and then have classes which inherit the planet base class for each of the planets in the  
# solar system. Each planet must have: distance to the sun, orbital period, and 2 interesting bits of information
# We then must make a class called SolarSystem which contains all the planets, has a method to print all the info for each planet, 
# and a method that inputs a number in days, and prints the number of times each planet has orbited the sun
# Owner: Dominic Pontious

from planetClass import Planet

class Mercury(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 {<str> : <int>}
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a dictionary as data1 and list as data2
		Input:	None
		Output: None
		"""

		data1 = {"Caloris Basin": 1550, "Tolstoj Basin": 400, "Beethoven Basin": 625}
		data2 = ["Galileo", "Gassendi", "Kepler", "Zupi"]
		Planet.__init__(self, "Mercury", 57910000, 87.969, data1, data2)
	
	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printDoubleTable(self,25, "Basin Name", 20, "Depth in Kilometers", self.data1)
		Planet.printSingleTable(self, 25, "Famous Telescopic Observers", self.data2)


class Venus(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 =  ["MESSENGER", "Venus Express", "Magellan", "Vega 2", "Vega 1", "Venera 16"]
		data2 = ["No moons oh my"]
		Planet.__init__(self, "Venus", 67240000, 225., data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self, 35, "Past Space Missions", self.data1)
		Planet.printSingleTable(self, 35, "Known Moons", self.data2)


class Earth(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
		data2 = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]
		Planet.__init__(self, "Earth", 92960000, 365.25, data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self,25,"Oceans", self.data1)
		Planet.printSingleTable(self,30, "Continents", self.data2)


class Mars(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""
	
	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 = ["2001 Mars Odyssey", "Mars Express", "Mars Reconnaissance Orbiter", "MAVEN", "Mars Obiter Mission", "ExoMars Trace Gas Orbiter"]
		data2 = ["Phobos", "Deimos"]
		Planet.__init__(self, "Mars", 141600000, 687, data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self, 35, "Misssions to Mars!", self.data1)
		Planet.printSingleTable(self, 25, "Moons", self.data2)


class Jupiter(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 = ["Pioneer program", "Voyager program", "Ulysses", "Cassini", "New Horizons", "Galileo", "Juno"]
		data2 = ["Io", "Europa", "Ganymede", "Callisto"]
		Planet.__init__(self, "Jupiter", 483800000, (365.25*12), data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self, 30, "Missions including Jupiter", self.data1)
		Planet.printSingleTable(self, 25, "Moons of Jupiter", self.data2)
				


class Neptune(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 = ["Voyager 2"]
		data2 = ["Triton", "Nereid", "Proteus", "Naiad", "Thalassa", "Despina", "Galatea"]
		Planet.__init__(self, "Neptune", 2793000000, (165*365.25), data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self, 30, "Missions including Neptune", self.data1)
		Planet.printSingleTable(self, 25, "Moons of Neptune", self.data2)


class Uranus(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 = ["Voyager 2"]
		data2 = ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]
		Planet.__init__(self, "Uranus", 1784000000, (84 * 365.25), data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self, 30, "Missions including Uranus", self.data1)
		Planet.printSingleTable(self, 25, "Moons of Uranus", self.data2)


class Saturn(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 = ["Pioneer 11", "Voyager 1", "Voyager 2", "Cassini/Huygens"]
		data2 = ["Titan", "Rhea", "Enceladus"]
		Planet.__init__(self, "Saturn", 890700000, (29*365.25), data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self, 30, "Missions including Saturn", self.data1)
		Planet.printSingleTable(self, 25, "Moons of Saturn", self.data2)


class Pluto(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 [<str>]
				data2 [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() from Planet class
				info(self) Calls Planet.info() from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.info() from Planet class, overloads with specific information for 
		 this planet, and adds a list for data1 and data2
		Input:	None
		Output: None
		"""

		data1 = ["Named after the Roman god of the underworld", "1930 Walt was inspired to use the name for the canine companion"]
		data2 = ["Charon", "Styx", "Nix", "Kerberos", "Hydra"]
		Planet.__init__(self, "Pluto", 3670000000, (248*365), data1, data2)

	def info(self):
		"""
		Calls Planet.info() from Planet class and adds print statements for the new data1 and data2
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTable(self, 45, "Fun facts", self.data1)
		Planet.printSingleTable(self, 25, "Moons of Pluto", self.data2)