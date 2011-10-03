#! /usr/bin/env python

import unittest
from math import sqrt, pi, cos, sin
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
				self.asteroids[objID] = object
		return objID

	def radar(self, position, range):
		"""
		Returns all objects within a certain radius of a position
		
		@param position: Position of the object to get radar
		@param range: Range of the radar
		"""
		return [object for object in self.objects.itervalues()
				if distance(position, object.position) <= range]

def map_maker(players):
	from game_instance import Game
	from planet import Planet, Base
	from asteroid import Asteroid
	from ship import Ship
	"""
	Adds initial planets, bases, and ships to the map.
	"""
	player_count = len(players)
	origin = (0,0)
	modifier = player_count * 5000
	angle = 2*pi/player_count
	i = 0
	for player in players.itervalues():
		x = modifier*cos((angle*i))
		y = modifier*sin((angle*i))
		size = randrange(500,1000,100)
		planet = Planet((x,y),size)
		base = Base(planet, player)
		ship = Ship((x+size*1.1, y+size), player)
		i += 1
	for x in range(player_count*10):
		x = randrange(-1.5*modifier, 1.5*modifier)
		y = randrange(-1.5*modifier, 1.5*modifier)
		size = randrange(100,500)
		asteroid = Asteroid((x,y),size)
		


class TestGame(unittest.TestCase):

	def setUp(self):
		from ship import Ship
		from player import Player
		self.m = Map(4)
		self.p = Player("a", "b")
		self.s = Ship((1,2), self.p)
		

	def test_create(self):
		self.assertTrue(self.m.max_players == 4)
		self.assertTrue(self.m.origin == (0,0))


	def test_add_object(self):
		self.m.add_object(self.s)
		self.assertTrue(len(self.m.objects) == 1)


	def test_radar(self):
		self.m.add_object(self.s)
		self.assertTrue(self.m.radar((1,2), 0)[0] == self.s)
		self.assertTrue(len(self.m.radar((2,2), 0)) == 0)

if __name__=='__main__':
	unittest.main()
