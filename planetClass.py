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

	def __init__(self, name = "none", distance = 1, orbitalPeriod = .1):
		"""
		Initializes a Planet class with the following parameters
		Input:	name <str>
				distance <int>
				orbitalPeriod <float>
		"""

		self.name = name
		self.distance = distance
		self.orbitalPeriod = orbitalPeriod

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

		print("The planet {} is {} miles to the sun!\nIt takes {} Earth days to orbit the sun!\n".format(self.getName(),\
		      self.getDistance(), self.getOrbitalPeriod()))

	def printSingleTableList(self, tableTitle, data):
		"""
			Takes in the title of the information being displayed and a list containing the data and 
			 formats a nice print statement
			Input: 	tableTitle <str>
					data [<str>]
			Output: None
		"""

		# Calculates the longest length of the strings to use to format the table
		maxStringLength = len(tableTitle)

		for dataString in data:
			if len(dataString) > maxStringLength:
				maxStringLength = len(dataString)

		# Prints the table name
		print("  {:^{}} \n".format(tableTitle, maxStringLength))

		# Prints a top border for the data
		print("\ {:-^{}} /".format("",maxStringLength))
		
		# Prints each element and puts a border on the sides
		for element in data:
			print("| {:^{}} |".format(element, maxStringLength))
		
		# Prints a bottom border for the data
		print("/ {:-^{}} \ ".format("",maxStringLength))
		print("\n")

	def printDoubleTableDict(self, keyTableTitle, valueTableTitle, data):
		"""
			Takes in two strings which are the titles for the keys and values respectively, 
			goes through the dictionary data and prints the information in a nice table format
			Input:	keyTableTitle <str>
					valueTableTitle <str>
					data {<str>: int}
			Output: None

		"""

		# Calculates the longest length of the dictionary keys and values as a string
		maxLengthKey = len(keyTableTitle)
		maxLengthValue = len(valueTableTitle)

		for key in data.keys():

			if len(key) > maxLengthKey:
				maxLengthKey = len(key)

			if len( str( data[key])) > maxLengthValue:
				maxLengthValue = len( str( data[key]))


		# Prints the Table Titles with some extra spacing
		print("{:^{}}     {:^{}}\n".format(keyTableTitle, maxLengthKey + 5, valueTableTitle, maxLengthValue + 5))

		# Prints a top border for the table
		print("\ {:-^{}} /".format("", maxLengthKey + maxLengthValue + 12))
		
		# Prints the information and puts a border on either side
		for elementKey in data:
			print ("| {:^{}} | {:^{}}| ".format(elementKey, maxLengthKey + 5, data[elementKey], maxLengthValue + 5))
		
		# Prints a bottom border for the table
		print("/ {:-^{}} \ ".format("", maxLengthKey + maxLengthValue + 12))
		print("\n")


