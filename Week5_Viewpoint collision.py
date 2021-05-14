import viz

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.MainView.setPosition([5, 1.82, -15])

viz.addChild('playground.wrl')
viz.clearcolor(viz.SKYBLUE)
viz.MainView.collision(viz.ON)

viz.MainView.gravity(2)

viz.MainView.stepsize(0.5)

quad = viz.addTexQuad()
quad.setScale([2,8.5,1])
quad.setEuler([0,79,0])
quad.setPosition([10,1.2,-1.22])

quad.alpha(0)