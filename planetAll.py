#!/usr/bin/env python3

# Homework Assignment 2+
# Requirements: Create a planet class and then have classes which inherit the planet base class for each of the planets in the  
# solar system. Each planet must have: distance to the sun, orbital period, and 2 interesting bits of information
# We then must make a class called SolarSystem which contains all the planets, has a method to print all the info for each planet, 
# and a method that inputs a number in days, and prints the number of times each planet has orbited the sun
# Owner: Dominic Pontious

class Planet(object):
	def __init__(self, name = "none", distance = 1, orbitalPeriod = .1, data1 = None, data2 = None):
		self.name = name
		self.distance = distance
		self.orbitalPeriod = orbitalPeriod
		self.data1 = data1
		self.data2 = data2

	def getName(self):
		return self.name

	def getDistance(self):
		return self.distance

	def getOrbitalPeriod(self):
		return self.orbitalPeriod

	def getData1(self):
		return self.data1

	def getData2(self):
		return self.data2

	def setName(self, name):
		self.name = name

	def setDistance(self, distance):
		self.distance = distance

	def setOrbitalPeriod(self, orbitalPeriod):
		self.orbitalPeriod = orbitalPeriod

	def setData1(self, data1):
		self.data1 = data1

	def setData2(self, data2):
		self.data2 = data2

	def info(self):
		return ("The planet " + self.getName() + " is " + str(self.getDistance()) + " km to the sun and takes " \
			+ str(self.getOrbitalPeriod()) + " Earth days to orbit the sun!")

class Mercury(Planet):

	def __init__(self):
		data1 = ["Caloris Basin: 1550km wide", "Tolstoj Basin: 400 km wide", "Beethoven Basin: 625 km wide"]
		data2 = ["Galileo", "Gassendi", "Kepler", "Zupi"]
		Planet.__init__(self, "Mercury", 57910000, 87.969, data1, data2)

class Venus(Planet):

	def __init__(self):
		data1 =  ["MESSENGER", "Venus Express", "Magellan", "Vega 2", "Vega 1", "Venera 16"]
		data2 = ["No moons oh my"]
		Planet.__init__(self, "Venus", 67240000, 225., data1, data2)

class Earth(Planet):

	def __init__(self):
		oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
		continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]
		Planet.__init__(self, "Earth", 92960000, 365.25, oceanList, continentList)

class Mars(Planet):
	def __init__(self):
		data1 = ["2001 Mars Odyssey", "Mars Express", "Mars Reconnaissance Orbiter", "MAVEN", "Mars Obiter Mission", "ExoMars Trace Gas Orbiter"]
		data2 = ["Phobos", "Deimos"]
		Planet.__init__(self, "Mars", 141600000, 687, data1, data2)

class Jupiter(Planet):

	def __init__(self):
		data1 = ["Pioneer program", "Vyager program", "Ulysses", "Cassini", "New Horizons", "Galileo", "Juno"]
		data2 = ["Io", "Europa", "Ganymede", "Callisto"]
		Planet.__init__(self, "Jupiter", 483800000, (365.25*12), data1, data2)

class Neptune(Planet):

	def __init__(self):
		data1 = ["Voyager 2"]
		data2 = ["Triton", "Nereid", "Proteus", "Naiad", "Thalassa", "Despina", "Galatea"]
		Planet.__init__(self, "Neptune", 2793000000, (165*365.25), data1, data2)

class Uranus(Planet):

	def __init__(self):
		data1 = ["Voyager 2"]
		data2 = ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]
		Planet.__init__(self, "Uranus", 1784000000, (84 * 365.25), data1, data2)

class Saturn(Planet):

	def __init__(self):
		data1 = ["Pioneer 11", "Voyager 1", "Voyager 2", "Cassini/Huygens"]
		data2 = ["Titan", "Rhea", "Enceladus"]
		Planet.__init__(self, "Saturn", 890700000, (29*365.25), data1, data2)

class Pluto(Planet):

	def __init__(self):
		data1 = ["Named after the Roman god of the underworld", "1930 Walt was inspired to use the name for the canine companion"]
		data2 = ["Charon", "Styx", "Nix", "Kerberos", "Hydra"]
		Planet.__init__(self, "Pluto", 3670000000, (248*365), data1, data2)



class SolarSystem(object):

	def __init__(self):
		self.mer = Mercury()
		self.ven = Venus()
		self.ear = Earth()
		self.mar = Mars()
		self.jup = Jupiter()
		self.sat = Saturn()
		self.ura = Uranus()
		self.nep = Neptune()
		self.plu = Pluto()
	

	def infoPlanet(self, planet):
		print("Name: " + planet.getName() + " distance to the sun " + str(planet.getDistance()) + "mi with orbital period: " \
		 + str(planet.getOrbitalPeriod()) + "\ndata1: ")
		for element in planet.getData1():
			print(element)
		print("data2:")
		for element2 in planet.getData2():
			print(element2)

	def info(self):

		self.infoPlanet(self.mer)
		self.infoPlanet(self.ven)
		self.infoPlanet(self.ear)
		self.infoPlanet(self.mar)
		self.infoPlanet(self.jup)
		self.infoPlanet(self.sat)
		self.infoPlanet(self.ura)
		self.infoPlanet(self.nep)
		self.infoPlanet(self.plu)

	def orbitedTheSunPlanet(self,planet, days):
		print("Name: " + planet.getName() + " ratio of sun orbit " + str(planet.getOrbitalPeriod() / 365.25) + " orbits in " + str(days) + " days\n")

	def orbitedTheSun(self, days):
		self.orbitedTheSunPlanet(self.mer, days)
		self.orbitedTheSunPlanet(self.ven, days)
		self.orbitedTheSunPlanet(self.ear, days)
		self.orbitedTheSunPlanet(self.mar, days)
		self.orbitedTheSunPlanet(self.jup, days)
		self.orbitedTheSunPlanet(self.sat, days)
		self.orbitedTheSunPlanet(self.ura, days)
		self.orbitedTheSunPlanet(self.nep, days)
		self.orbitedTheSunPlanet(self.plu, days)

# I use the main function to test my classes
def main():
	ss = SolarSystem()
	# ss.info()
	ss.orbitedTheSun(100)

# This is just a check to make sure the script is being handled correctly
if (__name__ == "__main__"):
	main()

else:
	print("improper use of the script!")