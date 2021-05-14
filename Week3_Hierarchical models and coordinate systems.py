import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)
viz.addChild('ground_grass.osgb')
viz.MainView.setPosition([0,1.8,-10])

carousel = viz.addChild('carousel.wrl')
carousel.addAction(vizact.spin(0,1,0,20))

pole1 = viz.addChild('pole.wrl', parent = carousel)
pole2 = viz.addChild('pole.wrl', parent = carousel)
pole3 = viz.addChild('pole.wrl', parent = carousel)
pole4 = viz.addChild('pole.wrl', parent = carousel)

pole1.setPosition([2.5,0,0])
pole2.setPosition([-2.5,0,0])
pole3.setPosition([0,0,2.5])
pole4.setPosition([0,0,-2.5])

horse1 = viz.addChild('horse.wrl',parent = pole1)
horse1.setEuler([180,0,0])
horse2 = viz.addChild('horse.wrl',parent = pole2)
horse2.setEuler([180,0,0])
horse3 = viz.addChild('horse.wrl',parent = pole3)
horse3.setEuler([180,0,0])
horse4 = viz.addChild('horse.wrl',parent = pole4)
horse4.setEuler([180,0,0])