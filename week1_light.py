import viz
viz.go()

forest = viz.add('art/forest.ive')
a = viz.addAvatar ('vcc_male.cfg')
a.setEuler( [20,0,0])
a.setPosition([-.78,0,.3])
a.state(1)

viz.MainView.setPosition([-.75,1.8,4.2])
viz.MainView.setEuler( [-180, 4, 0])

viz.MainView.getHeadLight().disable()

moon_light = viz.addLight()
moon_light.position(0,1,0,0)
moon_light.color ( [.6,.7,.9])
moon_light.intensity(1)

moon_light.disable()

lantern = viz.add('art/lantern.ive')
lantern_position = [0.14,1.5,0.5]
lantern.setPosition( lantern_position)

lantern_light = viz.addLight()
lantern_light.position(0,0,0,1)

viz.link(lantern, lantern_light)

flame = lantern.getChild('flame')
flame.emissive(viz.YELLOW)

lantern_light.color(viz.YELLOW)
lantern_light.quadraticAttenuation(1)
lantern_light.intensity(8)

lantern.specular(viz.YELLOW)
lantern.shininess(10)

lantern_light.disable()

torch=viz.add('art/flashlight.IVE')
torch.setPosition( [-1.16, 1.78,1.63])
flash_light = viz.addLight()
flash_light.position(0,0,0,1)

flash_light.spread(45)
flash_light.spotexponent(40)
viz.link(torch, flash_light)

torch.addAction(vizact.spin(0,1,0,90, viz.FOREVER))