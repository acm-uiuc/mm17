#! /usr/bin/env python
""" Constants used in ship.py  """
base_size = 10
base_health = 100
scan_range = 2000
weapon_range = 1000
weapon_strength = 100

max_velocity = 50
max_accel = 5

refinery_price = 10
base_price = 50

""" Constants used in asteroid.py """
asteroid_scale = 10  # asteroid.resources = size * asteroidScale
resource_pull = 1    # Ammount of resources pulled from factories each turn

""" Constants used in players.py """
score_constant = 1

""" Constants used in planet.py """
planet_scale = 10000
repair_percent = 0.10
build_radius = 15
ship_price = 10

""" Constants used in validate.py """
base_build_radius = 15000
base_salvage_radius = 15000
base_repair_radius = 15000

base_build_busy = 5
base_salvage_busy = 5
base_repair_busy = 5


if __name__ == '__main__':
	# No unit tests for constants
	pass
