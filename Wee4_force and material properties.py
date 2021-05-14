import viz
import vizact
import vizinfo

viz.setMultiSample(4)
viz.fov(60)
viz.go()

vizinfo.InfoPanel(align=viz.ALIGN_RIGHT_BOTTOM)

viz.phys.enable()

boxInfo = vizinfo.InfoPanel('Box Material Characteristics', align=viz.ALIGN_LEFT_TOP)
boxInfo.addSeparator()
boxScale = boxInfo.addLabelItem('Scale',viz.addSlider())
boxDensity = boxInfo.addLabelItem('Density',viz.addSlider())
boxFriction = boxInfo.addLabelItem('Friction',viz.addSlider())
boxHardness = boxInfo.addLabelItem('Hardness',viz.addSlider())
boxBounce = boxInfo.addLabelItem('Bounce',viz.addSlider())
boxForce = boxInfo.addLabelItem('Force',viz.addSlider())

boxScale.set( .5 )
boxDensity.set( .5 )
boxForce.set( .3 )

ballInfo = vizinfo.InfoPanel( 'Ball Material Characteristics', align=viz.ALIGN_RIGHT_TOP)
ballInfo.addSeparator()
ballScale = ballInfo.addLabelItem('Scale',viz.addSlider())
ballDensity = ballInfo.addLabelItem('Density',viz.addSlider())
ballFriction = ballInfo.addLabelItem('Friction',viz.addSlider())
ballHardness = ballInfo.addLabelItem('Hardness',viz.addSlider())
ballBounce = ballInfo.addLabelItem('Bounce',viz.addSlider())
ballForce = ballInfo.addLabelItem('Force',viz.addSlider())

ballScale.set( .5 )
ballDensity.set( .5 )
ballForce.set( .3 )

lab = viz.addChild('lab.osgb')
lab.collideMesh()
lab.disable(viz.DYNAMICS)

box = viz.addChild( 'crate.osgb' )

ball = viz.addChild( 'beachball.osgb' )


def reset():

    boxStartPOS = [ -3, .75, 2 ]
    box.setPosition( boxStartPOS )
    box.setEuler( [0, 0, 0] )

    scaleFactor = boxScale.get() * 2
    box.setScale( [scaleFactor]*3 )

    box.collideNone()
    boxPhysicalShape = box.collideBox() 

    boxPhysicalShape.density = boxDensity.get()
    boxPhysicalShape.friction = boxFriction.get()
    boxPhysicalShape.hardness = boxHardness.get()
    boxPhysicalShape.bounce = boxBounce.get()

    box.applyForce( dir = [ 10 * boxForce.get(), 0, 0 ], duration=0.1, pos = boxStartPOS )

    ballStartPOS = [ 3, .5, 2 ]
    ball.setPosition( ballStartPOS )
    ball.setEuler( [0, 0, 0] )

    scaleFactor = ballScale.get() * 2
    ball.setScale( [scaleFactor]*3 )

    ball.collideNone() 
    ballPhysicalShape = ball.collideSphere()

    ballPhysicalShape.density = ballDensity.get()
    ballPhysicalShape.friction = ballFriction.get()
    ballPhysicalShape.hardness = ballHardness.get()
    ballPhysicalShape.bounce = ballBounce.get()

    ball.applyForce(dir = [-10 * ballForce.get(), 0, 0], duration=0.1, pos = ballStartPOS)


reset()

vizact.onkeydown( ' ', reset )

import vizcam
viz.cam.setHandler(vizcam.KeyboardCamera())

def pushObject():
    info = viz.pick( True )
    if info.valid and ( info.object == ball or info.object ==box ):
        line = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
        vec = viz.Vector( line.dir )
        vec.setLength( 1 )
        info.object.applyForce(dir = vec, duration = 0.1, pos = info.point)
        return True

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pushObject)

viz.MainView.setPosition([0, 2, -5])