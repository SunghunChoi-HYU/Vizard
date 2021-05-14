import viz
import math
import time
viz.go()

ground = viz.add('art/sphere_ground3.ive')
rod = viz.add('art/rod.ive')
fish = viz.add('art/pike.ive')
barrel = viz.add('art/barrel.ive')
avatar = viz.add ('vcc_male.cfg')

viz.clearcolor( [.5,.6,2] )
viz.MainView.setPosition(-7,1.5,.33)
viz.MainView.setEuler(90,0,0)

fish.parent(rod)
fish.setPosition( [.06,.04,2.28], viz.ABS_PARENT)
fish.setEuler( [0,-45,190], viz.ABS_PARENT)
fish.setScale( [1,1,1.2], viz.ABS_LOCAL)

rod.setEuler( [0.0,-50.0,0.0], viz.ABS_GLOBAL)
rod.setPosition( [-.04,0.13,-1.14], viz.ABS_GLOBAL)

avatar.setPosition(2,0,0)

bees = avatar.add('art/bees.ive')
bees.setPosition ( [0,1.8,0], viz.ABS_PARENT)

def swarm():
	bees.setEuler([5,0,0], viz.REL_PARENT)
vizact.ontimer(.01,swarm)

avatar.state(11)
def run_around():
	newX = -math.cos(time.clock()) *2.1
	newZ = math.sin(time.clock()) * 2.2
	avater.setPosition([newX,0,newz], viz.ABS_PARENT)
	avater.setEuler( [time.clock()/math.pi*180,0,0],viz.ABS_PARENT)
vizact.ontimer(.01, run_around)