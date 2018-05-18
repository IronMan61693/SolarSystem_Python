#!/usr/bin/env python3

# Homework Assignment 2+
# Requirements: Create a planet class and then have classes which inherit the planet base class for each of the planets in the  
# solar system. Each planet must have: distance to the sun, orbital period, and 2 interesting bits of information
# We then must make a class called SolarSystem which contains all the planets, has a method to print all the info for each planet, 
# and a method that inputs a number in days, and prints the number of times each planet has orbited the sun
# Owner: Dominic Pontious

from specificPlanetsClasses import *

import sys


class SolarSystem(object):

	def __init__(self):
		"""
		Initializes the SolarSystem class with instances of each of the desired planet classes, creates a list of the planet instances
		 creates a list of the names of the planet classes
		Input: 	None
		Output: None
		"""

		self.mercury = Mercury()
		self.venus = Venus()
		self.earth = Earth()
		self.mars = Mars()
		self.jupiter = Jupiter()
		self.saturn = Saturn()
		self.uranus = Uranus()
		self.neptune = Neptune()
		self.pluto = Pluto()
		self.planets = [self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn, self.uranus, self.neptune, self.pluto]
		self.planetNames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
	

	def info(self):
		"""
		Loops through each of the instanced planets in the planets[] and calls their info function
		Input: 	None
		Output: None
		"""

		for planet in self.planets:
			planet.info()
			print("\n")

	def infoSpecific(self,planetName):
		"""
		Loops through planets[] comparing the name of each planet class with the input planet name in order to call 
		the info function on that particular planet instance
		Input: 	planetName <str>
		Output: None
		"""

		for element in self.planets:
			if (planetName == element.getName()):
				element.info()
				print("\n")

	# Func to print the how much a planet has orbited given some days
	def orbitedTheSunPlanet(self, planet, days):
		"""
		Calculates how much a given input planet has orbited the sun given a number of input days
		Input:	planet <Planet>
				days <int>
		Output: None

		"""

		# This helps format the orbit nicely to only 2 decimal places
		orbited = days / planet.getOrbitalPeriod()
		if (orbited < .01):
			orbited = "{0:.2e}".format(orbited)

		else:
			orbited = "{0:.2f}".format(orbited)


		print("{:<15} {:<15} {:<15}".format(planet.getName(), orbited, days))

	# Uses a loop to call orbitedTheSunPlanet() on every planet in planets list 
	def orbitedTheSun(self, days):
		"""
		Uses a loop to call the orbitedTheSunPlanet() on every planet in the planets list
		Input:	days <int>
		Output: None
		"""

		print("\n{:<15} {:<15} {:<15}\n".format("Planet Name:", "Orbit Ratio", "Days"))
		for planet in self.planets:
			self.orbitedTheSunPlanet(planet, days)


# I use the main function to test my classes
def main():

	# Instantiate a SolarSystem class
	solarsystem = SolarSystem()

	# User interface
	menuInput = 0

	# Allows the user to continue using the main with input values 1,2,3 
	while(menuInput!=3):
		menuInput = 0
		
		user_input = input('\nPress 1 if you would like to view the information of a planet in our solar system.\
		 \nPress 2 if you would like to input a number of days and see how much the planets orbited the sun.\
		 \nPress 3 if you would like to exit.\
		 \nHave a nice day! \n')

		# Verifies the input can be cast to an integer 
		try: 
			menuInput = int(user_input)

		except ValueError:
			print("This was not a useable input type. Please input a number")

	# This is an input to display information about the planets
		if (menuInput == 1):
			planet_input = input('Type solarsystem if you would like the information for the whole solar system.\
			\nOtherwise type the name of the planet you would like the information in the form Mercury, Venus. \n')

			# This calls the solarsystem info func
			if (planet_input == "solarsystem"):
				solarsystem.info()

			# This calls the planet info fun inside of the solarsystem
			elif (planet_input in solarsystem.planetNames):
				solarsystem.infoSpecific(planet_input)

			else:
				print("That is not a correctly named planet, it should be in the form Earth, Mars etc...")
				exit(3)

		elif (menuInput == 2):
			# Ask for user input to test orbitedTheSun()
			user_inputDays = input('How many days orbit would you like to check? \n')

			# Verify the input is a type we can use
			try: 
				day = float(user_inputDays)

				# Call the orbitedTheSun() func
				solarsystem.orbitedTheSun(day)

			except ValueError:
				print("That is not a number!")

			

		elif (menuInput == 3):
			exit(0)

		else:
			print("Please select one of the options")


# This is just a check to make sure the script is being handled correctly
if (__name__ == "__main__"):
	main()

else:
	print("improper use of the script!")