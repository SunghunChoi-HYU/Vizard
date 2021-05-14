import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

import vizinfo
vizinfo.InfoPanel(align=viz.ALIGN_LEFT_BOTTOM)

viz.clearcolor(viz.SLATE)

viz.phys.enable()

ground = viz.addChild('ground.osgb')
ground.collidePlane()

seesaw = viz.addChild('box.wrl')
seesaw.setScale([10,0.3,1])
seesaw.collideBox()

fulcrum = viz.addChild('tut_cone.wrl')
fulcrum.setScale([0.5,0.5,0.5])
fulcrum.setPosition([0,.01,1])
fulcrum.collideMesh() 
fulcrum.disable(viz.DYNAMICS)

load = viz.addChild('duck.wrl')
load.collideBox()

counterWeight = viz.addAvatar('duck.cfg')
counterWeight.collideBox(density=5)

viz.MainView.setPosition([0,2,-10])

def reset():
    seesaw.reset() 
    seesaw.setPosition([0,3,5])
    seesaw.setEuler([0,0,0])
    
    load.reset()
    load.setPosition([4,5,5])
    load.setEuler([0,0,0])

    counterWeight.reset()
    counterWeight.setPosition([-4, 11, 5])
    counterWeight.setEuler([90,0,0])

reset()

vizact.onkeydown(' ', reset)