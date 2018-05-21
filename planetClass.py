#!/usr/bin/env python3

# Homework Assignment 2+
# Requirements: Create a planet class and then have classes which inherit the planet base class for each of the planets in the  
# solar system. Each planet must have: distance to the sun, orbital period, and 2 interesting bits of information
# We then must make a class called SolarSystem which contains all the planets, has a method to print all the info for each planet, 
# and a method that inputs a number in days, and prints the number of times each planet has orbited the sun
# Owner: Dominic Pontious

class Planet(object):
	"""
	Variables:
				name <str>
				distance <int>
				orbitalPeriod <float>
				data1 <None>
				data2 <None>
	Methods:
				__init__(self) Initializes the Planet
				getName(self) Getter method for named variable
				getDistance(self) Getter method for named variable
				getOrbitalPeriod(self) Getter method for named variable
				getData1(self) Getter method for named variable
				getData2(self) Getter method for named variable
				setName(self, name) Setter method for named variable
				setDistance(self, distance) Setter method for named variable
				setOrbitalPeriod(self, orbitalPeriod) Setter method for named variable
				info(self) Print method for all class variables
				printSingleTable(self, columnSize, name, data) Print method for formatting a list
				printDoubleTable(self, leftColumnSize, name1, rightColumnSize, name2, data)
					Print method for formatting a dictionary
	"""

	def __init__(self, name = "none", distance = 1, orbitalPeriod = .1, data1 = None, data2 = None):
		"""
		Initializes a Planet class with the following parameters
		Input:	name <str>
				distance <int>
				orbitalPeriod <float>
				data1 <None>
				data2 <None>
		"""
		self.name = name
		self.distance = distance
		self.orbitalPeriod = orbitalPeriod
		self.data1 = data1
		self.data2 = data2

	# The following are getters so we do not directly reference the data in the class
	def getName(self):
		"""
		Getter method for name variable
		Input: None
		Output: name <str>
		"""

		return self.name

	def getDistance(self):
		"""
		Getter method for distance variable
		Input: None
		Output: distance <int>
		"""

		return self.distance

	def getOrbitalPeriod(self):
		"""
		Getter method for orbitalPeriod variable
		Input: None
		Output: orbitalPeriod <float>
		"""

		return self.orbitalPeriod

	def getData1(self):
		"""
		Getter method for data1 variable
		Input: None
		Output: data1 <None>
		"""

		return self.data1

	def getData2(self):
		"""
		Getter method for data2 variable
		Input: None
		Output: data2 <None>
		"""

		return self.data2

	# These are the setters
	def setName(self, name):
		"""
		Setter method for name variable
		Input: name <str>
		Output: None
		"""

		self.name = name

	def setDistance(self, distance):
		"""
		Setter method for distance variable
		Input: distance <int>
		Output: None
		"""

		self.distance = distance

	def setOrbitalPeriod(self, orbitalPeriod):
		"""
		Setter method for orbitalPeriod variable
		Input: orbitalPeriod <float>
		Output: None
		"""

		self.orbitalPeriod = orbitalPeriod

	def info(self):
		"""
		Method which prints the name, distance and orbitalPeriod variables with some formatting
		Input:	None
		Output: None
		"""

		print("{}: \n".format(self.getName()))
		print("The planet {} is {} miles to the sun!\nIt takes {} Earth days to orbit the sun!\n".format(self.getName(), self.getDistance(),\
		 self.getOrbitalPeriod()))

	def printSingleTable(self,columnSize, name, data):
		"""
			Takes in desired column size, the name of the information being displayed and a list containing the data and 
			 formats a nice print statement
			Input: 	columnSize <int>
					name <str>
					data [<str>]
			Output: None
		"""
		print("  {:^{}} \n".format(name, columnSize))
		print("\ {:-^{}} /".format("",columnSize))
		for element in data:
			print("| {:^{}} |".format(element, columnSize))
		print("/ {:-^{}} \ ".format("",columnSize))
		print("\n")

	def printDoubleTable(self, leftColumnSize, name1, rightColumnSize, name2, data):
		"""
			Takes in two strings which describe the type of information being displayed, name1: what the key represents name2: the value, 
			goes through the dictionary data and prints the information in a nice table format, left and right column size denote the
			desired width of the columns
			Input:	leftColumnSize <int>
					name1 <str>
					rightColumnSize <int>
					name2 <str>
					data {<str>: int}
			Output: None

		"""
		print("{:^{}}     {:^{}}\n".format(name1, leftColumnSize, name2, rightColumnSize))
		print("\ {:-^{}} /".format("",leftColumnSize+rightColumnSize+2))
		for elementKey in data:
			print ("| {:^{}} | {:^{}}| ".format(elementKey, leftColumnSize, data[elementKey], rightColumnSize))
		print("/ {:-^{}} \ ".format("",leftColumnSize+rightColumnSize+2))
		print("\n")


