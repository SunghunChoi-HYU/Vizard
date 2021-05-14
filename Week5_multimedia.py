import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

mySound = viz.addAudio('bach_air.mid')
vizact.onkeydown('p', mySound.play)
vizact.onkeydown('s', mySound.stop)
mySound.loop(viz.ON)

duck = viz.addAvatar('duck.cfg')
duck.setEuler([180,0,0])
duckMove = vizact.sequence([vizact.moveTo([0,1,22],speed=2), vizact.moveTo([0,1,0],speed=2)], viz.FOREVER)
duck.addAction(duckMove)

quack = duck.playsound('quack.wav', viz.STOP)
vizact.onkeydown('q', quack.play, viz.LOOP)

myVideo = viz.addVideo('mona.mpg')
myScreen = viz.addChild('white_ball.wrl')
myScreen.texture( myVideo )
myScreen.setPosition([0.5,2,2])
myScreen.setEuler([-90,90,0])
myVideo.play()
myVideo.loop()