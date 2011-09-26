#! /usr/bin/env python

import unittest
from math import sqrt
from random import randrange

from vector import distance

class Map(object):
	"""
	Map class that contains objects
	"""
	def __init__(self, max_players):
		"""
		Initializes the game map
		
		@param max_players: The maximum number of players the map supports
		"""
		self.origin = (0, 0)
		self.max_players = max_players
		self.objects = {}
		self.ships = {}
		self.planets = {}
		self.asteroids = {}
		self.dicts = [self.objects,
				self.ships,
				self.planets,
				self.asteroids]

	def add_object(self, object):
		from ship import Ship
		from planet import Planet
		from asteroid import Asteroid
		"""
		Adds an object to the map's global object dictionary.
		
		@param object: Object to be added to the map
		"""
		objID = id(object)
		if objID not in self.objects.keys():
			self.objects[objID] = object
			if isinstance(object, Ship):
				self.ships[objID] = object
			if isinstance(object, Planet):
				self.planets[objID] = object
			if isinstance(object, Asteroid):
				self.asteroidss[objID] = object
		return objID

	def radar(self, position, range):
		"""
		Returns all objects within a certain radius of a position
		
		@param position: Position of the object to get radar
		@param range: Range of the radar
		"""
		return [object for object in self.objects.itervalues()
				if distance(position, object.position) <= range]

if __name__=='__main__':
	unittest.main()
