import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

piazza = viz.addChild('piazza.osgb')

male = viz.addAvatar('vcc_male.cfg',pos=[8, 0, 7])
female = viz.addAvatar('vcc_female.cfg',pos=[8,0,9],euler=[180,0,0])
male.state(14)
female.state(14)

bird1 = viz.addAvatar('pigeon.cfg',pos=[-6.5, 0.43, -1.56],euler=[120,0,0])
bird1.state(1)

bird2 = viz.addAvatar('pigeon.cfg',pos=[5.61, 4.5, -9.88],euler=[-90,0,0])
bird2.state(1)

piazza.playsound('fountain.wav',viz.LOOP,node='fountain-sound')

conversation_node = viz.addGroup(pos=[8,1.8,8])
conversation_node.playsound('conversation.wav',viz.LOOP)

bell_sound = piazza.playsound('bells.wav',node='bell-sound')
bell_sound.minmax(0,3)
vizact.onkeydown('1',bell_sound.play)
def startBird1():
    bird1_sound = bird1.playsound('birds.wav')
    vizact.ontimer(14,bird1_sound.play)

vizact.ontimer2(7,0,startBird1)

bird2_sound = bird2.playsound('birds.wav')
vizact.ontimer(14,bird2_sound.play)

def birdView():
    viz.MainView.setPosition([5.9,4.9,-10.2])
    viz.MainView.setEuler([-43.5,29,0])

vizact.onkeydown('2',birdView)

vizact.onkeydown(' ',viz.setDebugSound3D,viz.TOGGLE)