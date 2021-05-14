import viz

viz.setMultiSample(4)
viz.fov(60)
viz.go() 
envLeft = viz.addEnvironmentMap('townhall_L.jpg')  
skyLeft = viz.addCustomNode('skydome.dlc')
skyLeft.texture(envLeft)
envRight = viz.addEnvironmentMap('townhall_R.jpg')  
skyRight = viz.addCustomNode('skydome.dlc')
skyRight.texture(envRight)

skyLeft.disable(viz.RENDER_RIGHT)
skyRight.disable(viz.RENDER_LEFT)