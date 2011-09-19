import math
from math import sin, cos
import random

import Game
import Map
from vector import distance, circle_in_rect

# half of dispersion
angle_fuzz = (2*math.pi)/16

class Ship(object):
	"""The class for a Player's ship.  A Player must be authorized to access certain
	methods. Any method that returns info must do so in a dictionary. """

	def __init__(self, game, player, position):
		# refrences to other objects
		self.owner = player
		self.game = game
		
		# attribute itialization
		self.alive = True
		self.position = position
		self.velocity = (0,0)
		self.health = 100
		self.scan_range = 2000
		self.weapon_range = 1000
		self.weapon_strength = 100

		# max values
		self.max_velocity = 10
		self.max_accel = 2

		# holds all events to be processed for next turn handle
		self.events = []

	def step(self, dt):
		vx, vy = self.velocity
		x, y = self.position
		self.position = (x + dt*vx, y + dt*vy)

	def thrust(self, accel):
		"""Sets the velocity based on acceleration and current velocity.

		Arguments:
		accel - (x,y) acceleration tuple
		"""
		dx, dy = accel
		# test to see if the accel is greater than allowed max
		mag = sqrt(dx*dx + dy*dy)
		if mag > self.max_accel:
			scale = self.max_accel/mag
		else:
			scale = 1
		x, y = self.velocity
		self.velocity = (x+scale*dx, y+scale*dy)
		# scale doown to max velocity
		vel_mag = sqrt(self.velocity[0]**2, self.velocity[1]**2)
		vel_scale = max_velocity/vel_mag
		self.velocity = vel_scale * self.velocity
		

	def fire(self, angle):
		"""Fire at angle relative to the ship's direction.  The laser
		is instant and is a rectangle with a width of 10 and a length 
		of self.weapon_strength. Any object that intersects that 
		rectatngle takes damage.

		Arguments:
		angle - angle relative to ships direction as radians
		"""
		width = 10
		length = self.weapon_strength
		
		#angle is relative to ship's direction
		angle += self.angle
		
		w = width/2 
		# Four points, counter clockwise
		p_0 = (self.position[0] + w * cos(angle), 
		       self.position + w * -sin(angle))    
 		p_3 = (self.position[0] + w * -cos(angle), 
		       self.position + w * sin(angle))      
		p_1 = (p_0[0] + length * cos(angle), p_0[1] + length * sin(angle))
		p_2 = (p_1[0] + length * cos(angle), p_1[1] + length * sin(angle))  

		# rectangle of laser beam
		beam = (p_0, p_1, p_2, p_3)

		within_beam = [] # list for objects in beam
		for obj in self.game.game_map.objects:
			if circle_in_rect(beam, obj.position, obj.radius):
				within_beam.append(obj)

		if len(within_beam) == 0:
			# No object hit
			self.events.append(("shot", None))
		else:
			within_beam.sort(key=distance(self.position, obj.position))
			# Hit first in line, record id
			self.events.append(("shot", within_beam[0].id))
			# register damage with hit object
			dist = distance(self.position, within_beam[0].position)
			damage_amt = self.weapon_strength *(self.weapon_range - \
								    dist)/weapon_range 
			within_beam[0].events(("damage", self.id, damage_amt, )
					   

	def scan(self, ship):
		"""Returns fuzzzed info if ship is in range, or None"""
		# Multiply the returned distance by a random value
		dist = distance(self.position, ship.position)
		if dist < self.scan_range:
			dist_error = random.uniform(0.5,1.5)
			dist *= dist_error
			dx = ship.position[0] - self.position[0]
			dy = ship.position[1] - self.position[1]
			if dist == 0:
				return (0,0)
			else:
				angle = math.atan2(dy,dx)
				angle_error = random.uniform(-angle_fuzz,angle_fuzz)
				angle += angle_error
				if angle < -math.pi:
					angle += 2*math.pi
				elif angle > math.pi:
					angle -= 2*math.pi
			return angle, dist, ship.health
		else: return None
