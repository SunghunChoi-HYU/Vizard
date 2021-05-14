import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

female = viz.addAvatar('vcc_female.cfg')
female.setPosition([0,0,3])
female.setEuler([180,0,0])
female.state(12)  

neck = female.getBone('Bip01 Neck')
neck.lock()

female.getBone('Bip01 Head').lock()

torso = female.getBone('Bip01 Spine1')
torso.lock()  

def faceView():
    viewPOS = viz.MainView.getPosition()
    neck.lookAt( viewPOS, mode=viz.AVATAR_WORLD )
    neckOrientation = neck.getEuler( viz.AVATAR_LOCAL )

    if neckOrientation[0] < -90 and neckOrientation[0] > -180: # -
        torso.setEuler([neckOrientation[0] + 90, 0, 0], viz.AVATAR_LOCAL)
        neck.lookAt( viewPOS, mode=viz.AVATAR_WORLD )

    elif neckOrientation[0] > 90 and neckOrientation[0] < 180: 
        torso.setEuler([neckOrientation[0] - 90, 0, 0], viz.AVATAR_LOCAL)
        neck.lookAt(viewPOS, mode=viz.AVATAR_WORLD)

vizact.ontimer(0, faceView)