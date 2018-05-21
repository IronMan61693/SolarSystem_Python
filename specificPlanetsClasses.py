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
				basins {<str> : <int>}
				notableObservers [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and for this planet, adds a dictionary for basins and list for notableObservers
		Input:	None
		Output: None
		"""

		self.basins = {"Caloris Basin": 1550, "Tolstoj Basin": 400, "Beethoven Basin": 625}
		self.notableObservers = ["Galileo", "Gassendi", "Kepler", "Zupi"]
		Planet.__init__(self, "Mercury", 57910000, 87.969)
	
	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printDoubleTableDict(self, "Basin Name", "Depth in Kilometers", self.basins)
		Planet.printSingleTableList(self, "Famous Telescopic Observers", self.notableObservers)


class Venus(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				spaceMissions [<str>]
				moons [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.spaceMissions =  ["MESSENGER", "Venus Express", "Magellan", "Vega 2", "Vega 1", "Venera 16"]
		self.poets = {"Homer": "Iliad", "Virgil" : "Eclogues", "William Blake" : "To The Evening Star",\
					  "Robert Frost" : "Literate Farmer and The Planet Venus", "Alfred Lord Tennyson" : "Crossing the Bar",\
					  "Stephen King": "The Cursed Expidition"}
		Planet.__init__(self, "Venus", 67240000, 225.)

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Past Space Missions", self.spaceMissions)
		Planet.printDoubleTableDict(self, "Poets", "The work which referenced Venus", self.poets)


class Earth(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				oceans [<str>]
				continents [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
		self.continents = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]
		Planet.__init__(self, "Earth", 92960000, 365.25)

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Oceans", self.oceans)
		Planet.printSingleTableList(self, "Continents", self.continents)


class Mars(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				spaceMissions [<str>]
				moons [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""
	
	def __init__(self, spaceMissions = [], moons = []):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.spaceMissions = ["2001 Mars Odyssey", "Mars Express", "Mars Reconnaissance Orbiter", "MAVEN", "Mars Obiter Mission",\
		 		 			  "ExoMars Trace Gas Orbiter"]
		self.moons = ["Phobos", "Deimos"]
		Planet.__init__(self, "Mars", 141600000, 687)

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Misssions to Mars!", self.spaceMissions)
		Planet.printSingleTableList(self, "Moons", self.moons)


class Jupiter(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				spaceMissions [<str>]
				moons [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.spaceMissions = ["Pioneer program", "Voyager program", "Ulysses", "Cassini", "New Horizons", "Galileo", "Juno"]
		self.moons = ["Io", "Europa", "Ganymede", "Callisto"]
		Planet.__init__(self, "Jupiter", 483800000, (365.25*12))

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Missions including Jupiter", self.spaceMissions)
		Planet.printSingleTableList(self, "Moons of Jupiter", self.moons)
				


class Neptune(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				spaceMissions [<str>]
				moons [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.spaceMissions = ["Voyager 2"]
		self.moons = ["Triton", "Nereid", "Proteus", "Naiad", "Thalassa", "Despina", "Galatea"]
		Planet.__init__(self, "Neptune", 2793000000, (165*365.25))

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Missions including Neptune", self.spaceMissions)
		Planet.printSingleTableList(self, "Moons of Neptune", self.moons)


class Uranus(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				spaceMissions [<str>]
				moons [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.spaceMissions = ["Voyager 2"]
		self.moons = ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]
		Planet.__init__(self, "Uranus", 1784000000, (84 * 365.25))

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Missions including Uranus", self.spaceMissions)
		Planet.printSingleTableList(self, "Moons of Uranus", self.moons)


class Saturn(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				spaceMissions [<str>]
				moons [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.spaceMissions = ["Pioneer 11", "Voyager 1", "Voyager 2", "Cassini/Huygens"]
		self.moons = ["Titan", "Rhea", "Enceladus", "Mimas", "Dione", "Iapetus"]
		Planet.__init__(self, "Saturn", 890700000, (29*365.25))

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Missions including Saturn", self.spaceMissions)
		Planet.printSingleTableList(self, "Moons of Saturn", self.moons)


class Pluto(Planet):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				funFact [<str>]
				moons [<str>]
	Methods:
				__init__(self) Initializes the Planet with the given information, and calls
					Planet.info() and printTable methods from Planet class
				info(self) Calls Planet.info() and printTable methods from Planet class and adds more print statements

	"""

	def __init__(self):
		"""
		Calls Planet.__init__ and adds variables for the new specific information for this planet 
		Input:	None
		Output: None
		"""

		self.funFact = ["Named after the Roman god of the underworld",
						"1930 Walt was inspired to use the name for the canine companion",
						"ReClassified a dwarf planet in 2006",
						"Discovered in 1930"
						"Is one third water"]
		self.moons = ["Charon", "Styx", "Nix", "Kerberos", "Hydra"]
		Planet.__init__(self, "Pluto", 3670000000, (248*365))

	def info(self):
		"""
		Calls Planet.info() and printTable methods from Planet class and adds print statements for the new information
		Input:	None
		Output: None
		"""

		Planet.info(self)
		Planet.printSingleTableList(self, "Fun facts", self.funFact)
		Planet.printSingleTableList(self, "Moons of Pluto", self.moons)