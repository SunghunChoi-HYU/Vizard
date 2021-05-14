import viz
import viztask
viz.go()

env = viz.add(viz.ENVIRONMENT_MAP, 'sky.jpg')
dome = viz.add('skydome.dlc')
dome.texture(env)

maze = viz.add('art/maze.ive')

balloons =[]
for pos in [ [.2,3.4],[-3.2,6.8],[-9.8,23.4],[6.4,30.2],[-13.0,33.4]]:
	balloon = viz.add('art/balloon.ive')
	balloon.setScale(2,2,2)
	balloon.setPosition(pos[0],1.7,pos[1])
	balloon.color(viz.RED)
	balloon.specular(viz.WHITE)
	balloon.shininess(128)
	balloons.append(balloon)

pop = viz.addAudio('art/pop.wav')
viz.collision(viz.ON)
viz.collisionbuffer(.1)

subwindow = viz.addWindow()
subview = viz.addView()
subwindow.setView(subview)
subwindow.setSize(.35,.35)
subwindow.setPosition(.65,1)
subwindow.visible(viz.OFF)

subview_link = viz.link(viz.MainView, subview)
subview_link.setMask(viz.LINK_POS)
subview_link.setOffset( [0,8,0])
subview.setEuler([0,90,0])

dart = viz.add('art/dart.ive')
dart.setScale(2,2,2)
link = viz.link(viz.MainView, dart)
link.preTrans( [0,.15,0])

text_dict = {}
for kind in ['score', 'instructions', 'time']:
	text = viz.addText('', viz.SCREEN)
	text.setScale(.5,.5)
	text.alignment(viz.TEXT_CENTER_BASE)
	text.alpha(1)
	text_dict[kind] = text
text_dict['score'].setPosition(.1,.9)
text_dict['instructions'].setPosition(.5,.5)
text_dict['time'].setPosition(.1,.85)

blank_screen = viz.addTexQuad(viz.SCREEN)
blank_screen.color (viz.BLACK)
blank_screen.setPosition(.5,.5)
blank_screen.setScale(100,100)

def set_the_stage():
	viz.MainView.setPosition(0,1.8,-3)
	viz.MainView.setEuler(0,0,0)
	viz.mouse(viz.OFF)
	text = text_dict['instructions']
	text.alpha(1)
	text.message('Prees s to begin.')
	yield viztask.waitKeyDown('s')
	text.message('')
viztask.schedule(set_the_stage())

def game_instructions():
	text = text_dict['instructions']
	text.alpha(1)
	sentences = ['You will get one point for each balloon that you pop.', 'You are racing against the clock.', 'Get ready . . .']
	for sentence in sentences:
		text.alpha(0)
		text.message(sentence)
		yield viztask.addAction(text, vizact.fadeTo(1, time = 1))
		yield viztask.waitTime(1)
		yield viztask.addAction(text, vizact.fadeTo(0, time = 1))

viztask.schedule(game_instructions())

def game_timer_task():
	text = text_dict['time']
	text.alpha(1)
	text.message("Time : 0")
	time = 0
	while time < 30:
		yield viztask.waitTime(1)
		time +=1
		text.message("Time : " + str(time))

def balloon_popping_task():
	text = text_dict['score']
	text.alpha(1)
	score = 0
	text.message("Score : 0")
	while score < 5:
		data = viz.Data()
		data = yield viztask.waitEvent(viz.COLLISION_EVENT)
		intersected_object = data.data[0].object
		if balloons.count(intersected_object):
			pop.play()
			score+=1
			text.message("Score : " + str(score))
			intersected_object.visible(viz.OFF)

def game() :
	viz.mouse(viz.ON)
	subwindow.visible(viz.ON)
	blank_screen.visible(viz.OFF)
	
	balloon_popping = viztask.waitTask(balloon_popping_task())
	time_passing = viztask.waitTask(game_timer_task())
	data = viz.Data()
	data = yield viztask.waitAny( [balloon_popping, time_passing])
	
	viz.mouse(viz.OFF)
	blank_screen.visible(viz.ON)
	subwindow.visible(viz.OFF)
	viz.MainView.reset(viz.HEAD_ORI | viz.HEAD_POS|viz.BODY_ORI)
	
	text = text_dict['instructions']
	if data.condition == balloon_popping:
		text.message("GAME OVER, YOU WON!")
	elif data.condition == time_passing:
		text.message("GAME OVER, YOU LOST!")
	text.alpha(1)
	text_dict['score'].alpha(0)
	text_dict['time'].alpha(0)
	yield viztask.waitTime(4)

def play_again():
	text_dict['instructions'].message('Want to play again (y/n)?')
	data = viz.Data()
	data= yield viztask.waitKeyDown(('n','y'))
	if data.key == 'n':
		viz.quit()
	if data.key == 'y':
		for balloon in balloons:
			balloon.visible (viz.ON)
		for value in text_dict.values():
			value.alpha(0)

def main_sequence():
	while True:
		yield set_the_stage()
		yield game_instructions()
		yield game()
		yield play_again()
	
viztask.schedule(main_sequence())