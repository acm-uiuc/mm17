from time import gmtime, strftime
import os

from game_map import Map
from game import Game

try:
	os.mkdir('logs')
except OSError:
	pass
viz_auth = '123456'
game_time = strftime("%Y-%m-%d-%H:%M:%S", gmtime())
log_file = 'logs/game-%s' % game_time
inited = False
# These values should be inited somewhere else
# XXX: Old test cases rely on them being inited here
game_map = Map(1)
game = Game(game_map, log_file, viz_auth)
