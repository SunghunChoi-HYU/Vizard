import viz
import vizact
import random

viz.setMultiSample(4)
viz.go()
viz.MainWindow.fov(60)
piazza = viz.addChild('piazza.osgb')
viz.collision(viz.ON)

viz.MainView.move([3,0,-7])

viz.move([0,0,-8])

plants=[]
for x in [-3,-1,1,3]:
	for z in [4,2,0,-2,-4]:
		plant = viz.addChild('plant.osgb', cache = viz.CACHE_CLONE)
		plant.setPosition([x,0,z])
		plant.setEuler([0,0,20])
		plants.append(plant)
		
spin = vizact.spin(0,1,0,15)
for plant in plants:
	plant.addAction(spin)
	
def spinPlant(plant):
	plant.addAction(spin)
vizact.ontimer2(0.5,19,spinPlant,vizact.choice(plants))

male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5,0,7])
male.setEuler([0,0,0])

female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0])

male.state(14)
female.state(14)

pigeons= []
for i in range(10):
	x = random.randint(-4,3)
	z = random.randint(4,8)
	yaw = random.randint(0,360)
	
	pigeon = viz.addAvatar('pigeon.cfg')
	
	pigeon.setPosition([x,0,z])
	pigeon.setEuler([yaw,0,0])
	pigeon.state(1)
	pigeons.append(pigeon)

def walkAvatars():
	walk1 = vizact.walkTo([4.5,0,-40])
	vizact.ontimer2(0.5,0,female.addAction,walk1)
	
	walk2 = vizact.walkTo([3.5,0,-40])
	male.addAction(walk2)
	
vizact.onkeydown('w', walkAvatars)

def pigeonsFeed():
	random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
	random_walk = vizact.walkTo(pos=[vizact.randfloat(-4,4),0,vizact.randfloat(3,7)])
	random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
	random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
	pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)

	for pigeon in pigeons:
		pigeon.addAction(pigeon_idle)

vizact.onkeydown('p',pigeonsFeed)