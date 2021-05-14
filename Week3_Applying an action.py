import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.addChild('ground.osgb')
wheel = viz.addChild('wheelbarrow.ive')
viz.MainView.move([0,0,-7])
viz.clearcolor(viz.SKYBLUE)

moveForward = vizact.move(0,0,2,1)
turnRight = vizact.spin(0,1,0,90,1)

wheel.addAction(moveForward)
wheel.addAction(turnRight)

moveInSquare = vizact.sequence(moveForward,turnRight,4)
wheel.addAction(moveInSquare)
vizact.onkeydown(' ', wheel.addAction, moveInSquare)
vizact.onkeydown('c', wheel.clearActions)