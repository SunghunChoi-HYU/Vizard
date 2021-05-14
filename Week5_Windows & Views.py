import viz

viz.setMultiSample(4)
viz.fov(60)
viz.go()

maze = viz.addChild('maze.osgb')

BirdEyeWindow = viz.addWindow()
BirdEyeWindow.fov(60)
BirdEyeView = viz.addView()
BirdEyeWindow.setView(BirdEyeView)

BirdEyeView.setPosition([0,25,0])
BirdEyeView.setEuler([0,90,0])

RearWindow = viz.addWindow()
RearWindow.fov(60)
RearView = viz.addView()
RearWindow.setView(RearView)
RearWindow.setPosition([0,1])

viewLink = viz.link( viz.MainView, RearView )
viewLink.preEuler([180, 0, 0])