import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

gallery = viz.addChild('gallery.osgb')

text3D = viz.addText3D('3D Text', pos = [0,2.5,4])
text3D.alignment(viz.ALIGN_CENTER_BOTTOM)
text3D.color(viz.BLUE)

text2D = viz.addText3D('2D Text', pos = [0,1,4])
text2D.alignment(viz.ALIGN_CENTER_BOTTOM)
text2D.resolution(1)
text2D.disable(viz.LIGHTING)

textScreen = viz.addText('Screen Text', viz.SCREEN)
textScreen.alignment(viz.ALIGN_RIGHT_BOTTOM)
textScreen.setPosition([0.95,0.05,0])

text3D.font('Times New Roman')

text3D.message('Art Gallery')

text2D.message('Starry Night')
text2D.setPosition([0, 3, 9.8])
text2D.setScale([0.4,0.4,0.4])

textScreen.message('')
def updateScreenText():
    object = viz.MainWindow.pick(info=True)
    if object.valid:
        name = object.name
        if name.startswith('painting_'):
            name = name.replace('painting_','')
            textScreen.message(name)
        else:
            textScreen.message('')

vizact.ontimer(0.1,updateScreenText)