import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

env = viz.addEnvironmentMap('sky.jpg')  

logo = viz.addChild('logo.ive')
logo.setPosition([0,1,3]) 
logo.texture(env)
logo.appearance(viz.ENVIRONMENT_MAP)
logo.addAction(vizact.spin(0,1,0,60))