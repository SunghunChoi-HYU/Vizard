import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

ground = viz.addChild('ground.osgb')
avatar = viz.addAvatar('vcc_male.cfg')

viz.MainView.move([0,10,-20])
viz.lookAt([0,0,0])

viz.mouse(viz.OFF) 

def avatarWalk():
    info = viz.pick(1)
    if info.valid and info.object == ground:
        walk = vizact.walkTo([info.point[0],0,info.point[2]])
        avatar.runAction(walk)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, avatarWalk)  

