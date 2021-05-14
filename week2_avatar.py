import viz
viz.go()

ground = viz.add('art/sphere_ground3.ive')
male = viz.add('vcc_male.cfg')
female = viz.add('vcc_female.cfg')
female.setPosition(-1,0,1)

env = viz.add(viz.ENVIRONMENT_MAP, 'sky.jpg')
dome = viz.add('skydome.dlc')
dome.texture(env)

viz.MainView.setPosition(0,1.8,5)
viz.MainView.setEuler(180,0,0)

female.state(1)
male.state(1)

bone_head = male.getBone('Bip01 Head')
bone_head.lock()

def follow_target() :
	f_pos = female.getPosition()
	m_pos = male.getPosition()
	f_point = [f_pos[0],f_pos[2]]
	m_point = [m_pos[0],m_pos[2]]
	angle = vizmat.AngleToPoint(m_point,f_point)
	if angle < 90 and angle > -90:
		bone_head.setEuler(angle, 0,0,viz.AVATAR_LOCAL)
vizact.ontimer(.01,follow_target)
vizact.onkeydown('d', male.blend, 5,1,5)
vizact.onkeydown('s', male.blend, 1,0,5)

female.setPosition(5,0,4)
walk_left = vizact.walkTo([-2,0,1])
walk_right = vizact.walkTo([3,0,1])
walking_sequence = vizact.sequence( [walk_left, walk_right], viz.FOREVER)
female.addAction(walking_sequence)

male.collideMesh()
ground.collideMesh()
ball = viz.add('soccerball.IVE')
ball.collideSphere()
ball.enable(viz.COLLIDE_NOTIFY)
ball.setPosition(100,100,100)

def onCollideBegin(e):
	if e.obj2 == male:
		male.execute(9, freeze = True)
		female.clearActions()
		female.execute(4)
viz.callback(viz.COLLIDE_BEGIN_EVENT,onCollideBegin)

def shoot_ball():
	ball.reset()
	ball.setPosition([1,2,5])
	ball.setVelocity([-2.8,.8,-15])
vizact.onkeydown(' ', shoot_ball)

def reset():
	male.stopAction(16)
	male.state(1)
	female.addAction(walking_sequence)
vizact.onkeydown('r',reset)

viz.phys.enable()