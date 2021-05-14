import viz
viz.go()

ground = viz.add('art/sphere_ground.ive')
avatar = viz.addAvatar ('vcc_female.cfg')
avatar.state(1)
balloons=[]

import random
for i in range(-5,6):
	for j in range(1,6):
		balloon = viz.add('art/balloon.ive')
		balloon.setPosition(i*.8,.1,j*.8)
		R = random.random()
		G = random.random()
		B = random.random()
		balloon.color (R,G,B)
		balloon.specular (viz.WHITE)
		balloon.shininess(128)
		balloons.append(balloon)
	
env = viz.add(viz.ENVIRONMENT_MAP, 'sky.jpg')
dome = viz.add('skydome.dlc')
dome.texture(env)

inflate_sound = viz.addAudio('art/blowballoon.wav')
deflate_sound = viz.addAudio('art/deflateballoon.wav')

for p in [1,-1]:
	light = viz.addLight()
	light.position(p,1,p,0)

viz.MainView.setPosition([0,1.2,-8.9])
viz.MainView.setEuler([0,-12,0])

INFLATED = [2,2,2]
DEFLATED = [.2,.2,.2]
BREATH_LENGHT = 3
DEFLATE_LENGTH = .1

grow = vizact.sizeTo( INFLATED, time = BREATH_LENGHT)
play_blowing_sound = vizact.call (inflate_sound.play)
inc_transparent = vizact.fadeTo(.7, begin=1, time = BREATH_LENGHT)
inflate = vizact.parallel (grow, play_blowing_sound,inc_transparent)

float_away = vizact.move(vizact.randfloat(-.2,.2),1,vizact.randfloat(-.2,.2) )
shrink = vizact.sizeTo(DEFLATED, time = DEFLATE_LENGTH)
play_def = vizact.call(deflate_sound.play)
dec_transparent = vizact.fadeTo(1, begin=.7, time = DEFLATE_LENGTH)
deflate = vizact.parallel(shrink, play_def, dec_transparent)

fall = vizact.fall(0)
random_wait = vizact.waittime(vizact.randfloat(.5,7))

life_cycle = vizact.sequence( [random_wait, inflate, float_away, deflate, fall],1)

for balloon in balloons:
	balloon.setScale(DEFLATED)
	vizact.onkeydown(' ', balloon.addAction, life_cycle)