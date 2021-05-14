import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

ground = viz.addChild('ground.osgb')

male = viz.addAvatar('vcc_male.cfg')
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([0,0,7])
female.setEuler([180,0,0])

female.state(1)
male.state(1)  

viz.MainView.setPosition([-6,1.8,3.5])
viz.MainView.setEuler([90,0,0])  

SHOUT_DURATION = female.getduration(3)

def heDances():
	male.addAction(vizact.animation(5))
	walk_over = vizact.walkTo([0,0,6])
	male.addAction(walk_over)
	male_turn_around = vizact.turn(90)
	male.addAction(male_turn_around)
	
def sheShouts():
    female.addAction(vizact.animation(3))
    vizact.ontimer2(SHOUT_DURATION, 0, heDances)

vizact.onkeydown('1', sheShouts)