import viz
viz.go()

viz.MainView.setPosition(0,1.8,-5)
tent = viz.add('art/tent.ive')
barrel = viz.add('art/barrel.ive')
ball = viz.add('soccerball.ive')

barrel.setEuler( [0,0,90])
barrel.setPosition([-1,.5,0])
ball.addAction( vizact.spin(0,1,0,360))
barrel.addAction (vizact.spin(0,1,0,-90))

female = viz.add('vcc_female.cfg')
female.setEuler(180,0,0)
female.state(2)

male = viz.add('vcc_male.cfg')
import debaser
debaser.pose_avatar(male, 'links_pose.txt')
male.setPosition([1,0,0])
male.setEuler(-45,0,0)
male.state(5)

finger_bone = male.getBone('Bip01 R Finger1Nub')
finger_link = viz.link(finger_bone,ball)

finger_link.setOffset([0,.1,0])
finger_link.setMaks(viz.LINK_POS)