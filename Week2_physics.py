import viz
import random
viz.go()

viz.MainView.getHeadLight().disable()
spot_light = viz.addLight()
spot_light.position(0,0,0,1)
spot_light.setEuler(180,65,180)
spot_light.setPosition(0,4.55,2.5)
spot_light.spread(45)
spot_light.spotexponent(5)
spot_light.intensity(1.5)

viz.MainView.setEuler(180,0,0)
viz.MainView.setPosition(0,1.5,6)

viz.mouse(viz.OFF)

tent = viz.add('art/tent.ive')
stand = viz.add('art/stand.ive')
wheel = viz.add('art/wheel.ive')
avatar = viz.add('vcc_male.cfg')
knife = viz.add('art/knife.ive')

wheel.setPosition([.02,1.62,.24])
wheel.setEuler([0,-20,0])

link = viz.link(wheel, avatar)
link.preTrans([0,-1,.1])
wheel.addAction (vizact.spin(0,0,1,90))

bones = ['L Thigh', 'R Thigh', 'L UpperArm', 'R UpperArm']
rolls = [-20,20,-40,40]
for i in range(len(bones)):
	bone = avatar.getBone('Bip01' + bones[i])
	bone.lock()
	bone.setEuler( [0,0,rolls[i]], viz.AVATAR_LOCAL)
avatar.idlepose(-1)

balloons = []
balloon_coords = [ [0,-.75],[.75,-.75],[-.75,-.75],[.5,0],[-.5,0],[.4,.9],[-.4,.9],[.9,.45],[-.9,.45]]
for coord in balloon_coords:
	balloon = viz.add('art/balloon2.ive')
	R = random.random()
	G = random.random()
	B = random.random()
	balloon.color(R,G,B)
	balloon.alpha(.8)
	balloon.specular(viz.WHITE)
	balloon.shininess(128)
	link = viz.link(wheel, balloon)
	link.preTrans ([coord[0],coord[1],0])
	link.preEuler([random.randrange(-60,60), random.randrange(100,150),0])
	balloons.append(balloon)
	
cry = viz.addAudio('art/grunt.wav')
avatar_hit = vizact.parallel(vizact.fadeTo(0,speed=1), vizact.call(cry.play))
avatar_sequence = vizact.sequence( [avatar_hit, vizact.fadeTo(1, speed = 1)],1)

popping_sound = viz.addAudio('art/pop.wav')
play_pop = vizact.call(popping_sound.play)
popping_action = vizact.sizeTo([.1,.2,.1],time = .5)
popping = vizact.parallel ([play_pop, popping_action])

wheel.collideMesh()
for ballon in balloons:
	balloon.collideMesh()
avatar.collideMesh()
ground = tent.getChild('ground')
ground.collidePlane(0,1,0,0)
knife.collideBox()
knife.enable(viz.COLLIDE_NOTIFY)

knife_link = 0

def stick_knife(into_what):
	global knife_link
	knife.disable(viz.PHYSICS)
	if knife_link :
		knife_link.remove()
	knife_link = viz.grab(into_what, knife)


def throw_knife():
	line = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
	vector = viz.Vector(line.dir)
	if knife_link :
		knife_link.remove()
	knife.reset()
	knife.enable(viz.PHYSICS)
	knife.setPosition(line.begin)
	knife.setEuler(180,90,0)
	knife.setVelocity(vector)
vizact.onmouseup(viz.MOUSEBUTTON_LEFT, throw_knife)

def onCollideBegin(e):
	if e.obj2 == avatar :
		avatar.addAction(avatar_sequence)
		stick_knife(avatar)
	if e.obj2 == wheel:
		stick_knife(wheel)
	if balloons.count(e.obj2):
		e.obj2.disable (viz.PHYSICS)
		e.obj2.addAction(popping)
		stick_knife(e.obj2)
	
viz.callback(viz.COLLIDE_BEGIN_EVENT,onCollideBegin)

def reset_balloons():
	for balloon in balloons:
		balloon.addAction(vizact.sizeTo([1,1,1], time =.5))
		balloon.enable(viz.PHYSICS)
vizact.onkeydown('r', reset_balloons)
viz.phys.enable()