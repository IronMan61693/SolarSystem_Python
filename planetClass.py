#!/usr/bin/env python3

# Homework Assignment 2+
# Requirements: Create a planet class and then have classes which inherit the planet base class for each of the planets in the  
# solar system. Each planet must have: distance to the sun, orbital period, and 2 interesting bits of information
# We then must make a class called SolarSystem which contains all the planets, has a method to print all the info for each planet, 
# and a method that inputs a number in days, and prints the number of times each planet has orbited the sun
# Owner: Dominic Pontious

class Planet(object):
	# These are the variables I want every planet to have
	def __init__(self, name = "none", distance = 1, orbitalPeriod = .1, data1 = None, data2 = None):
		self.name = name
		self.distance = distance
		self.orbitalPeriod = orbitalPeriod
		self.data1 = data1
		self.data2 = data2

	# The following are getters so we do not directly reference the data in the class
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

	# These are the setters
	def setName(self, name):
		self.name = name

	def setDistance(self, distance):
		self.distance = distance

	def setOrbitalPeriod(self, orbitalPeriod):
		self.orbitalPeriod = orbitalPeriod

	# This is a base print statement for Planet
	def info(self):

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
		for element in data:
			print("| {:^{}} |".format(element, columnSize))
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
		for elementKey in data:
			print ("| {:^{}} | {:^{}}| ".format(elementKey, leftColumnSize, data[elementKey], rightColumnSize))
		print("\n")


