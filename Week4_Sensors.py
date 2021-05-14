import viz
import vizact
import vizproximity
import viztask
import vizinfo

viz.setMultiSample(4)
viz.fov(60)
viz.go()

instructions = vizinfo.InfoPanel(icon=False,key=None)

piazzaSound = viz.addAudio('piazza.mp3')
piazzaSound.play()
piazzaSound.loop()

piazza = viz.add('piazza.osgb')

viz.MainView.move([10.5,0,20.5])
viz.MainView.setEuler([-90,0,0])

male = viz.addAvatar('vcc_male.cfg',pos=[-2.6,0,10.4],euler=[-40,0,0])
female = viz.addAvatar('vcc_female.cfg',pos=[-3.4,0,11.2],euler=[140,0,0])
male.state(14)
female.state(14)

pigeon = viz.addAvatar('pigeon.cfg')
pigeon.visible(0)

plantMarker = viz.addChild('plant.osgb',pos=[-10.3,0,20.6],scale=[0.5,0.5,0.5])

crate1 = viz.addChild('crate.osgb',pos=[-9.9,0.3,5.7],scale=[0.6,0.6,0.6])
crate2 = crate1.clone(pos=[-9.8,0.3,5.05],euler=[5,0,0],scale=[0.6,0.6,0.6])
crate3 = crate1.clone(pos=[-9.8,0.9,5.35],euler=[-5,0,0],scale=[0.6,0.6,0.6])

avoidSitting = True
avoidStanding = True
avoidDancing = True

pigeonPositions=[[-6.9,0,7.2],[3.3,0,14.5],[0.8,0,16],[-2.3,0,14.7],[2.9,0,-1.6],[-0.7,0,-1.7]]

for pos in pigeonPositions:
    pigeon = pigeon.copy(pos=pos)
    random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
    random_walk = vizact.walkTo(pos=[vizact.randfloat(pos[0]-0.3,pos[0]+0.3),0,vizact.randfloat(pos[2]-0.5,pos[2]+0.5)])
    random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
    random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
    pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)
    pigeon.runAction(pigeon_idle)

avatar1 = viz.addAvatar('vcc_male2.cfg',pos=[2.1,0, 21.4],euler=[180,0,0],scale=[0.95,0.95,0.95])
avatar2 = avatar1.copy(pos=[-10.2,0,12],euler=[90,0,0])
avatar3 = avatar1.copy(pos=[1.5,0,5.6],euler=[180,0,0])
avatar1.state(6)
avatar2.state(1)
avatar3.state(5)

plantSensor = vizproximity.Sensor(vizproximity.Box([4,5,5],center=[0,2.5,0]),source=plantMarker)
cratesSensor = vizproximity.Sensor(vizproximity.Box([5,4,4],center=[0,1.7,0]),source=crate1)
cafeSensor = vizproximity.Sensor(vizproximity.Box([5,4,10]),source=viz.Matrix.translate(12,2,7.5))

sensorAvatar1 = vizproximity.Sensor(vizproximity.Box([2,2.5,2.5],center=[0,1.3,1]),source=avatar1)
sensorAvatar2 = vizproximity.Sensor(vizproximity.Box([2,2.5,2.5],center=[0,1.3,0.7]),source=avatar2)
sensorAvatar3 = vizproximity.Sensor(vizproximity.Box([2,2.5,2.5],center=[0,1.3,0.7]),source=avatar3)

target = vizproximity.Target(viz.MainView)

manager = vizproximity.Manager()

manager.addSensor(plantSensor)
manager.addSensor(cratesSensor)
manager.addSensor(cafeSensor)

manager.addSensor(sensorAvatar1)
manager.addSensor(sensorAvatar2)
manager.addSensor(sensorAvatar3)

manager.addTarget(target)

vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

def destinationsTask():

    DelayHide = vizact.sequence(vizact.waittime(8), vizact.method.visible(False))
    Show = vizact.method.visible(True)

    yield viztask.waitTime(12)
    instructions.setText("Walk to the potted plant directly ahead on the opposite side of the courtyard.")
    instructions.runAction(DelayHide)
    yield vizproximity.waitEnter(plantSensor)
    instructions.runAction(Show)
    instructions.setText("Face the arch side of the courtyard. Walk to the piles of crates directly ahead.")
    instructions.runAction(DelayHide)
    yield vizproximity.waitEnter(cratesSensor)
    instructions.runAction(Show)
    instructions.setText("Walk into the cafe on the opposite side of the courtyard.")
    instructions.runAction(DelayHide)
    yield vizproximity.waitEnter(cafeSensor)
    instructions.runAction(Show)
    instructions.setText("Thank you for your participation.")

    print('Avoided sitting avatar:',avoidSitting)
    print('Avoided standing avatar:',avoidStanding)
    print('Avoided dancing avatar:',avoidDancing)

viztask.schedule(destinationsTask())

avoidSitting = True
avoidStanding = True
avoidDancing = True

def EnterProximity(e):

    global avoidSitting,avoidStanding,avoidDancing
    if e.sensor == sensorAvatar1:
        avoidSitting = False
    elif e.sensor == sensorAvatar2:
        avoidStanding = False
    elif e.sensor == sensorAvatar3:
        avoidDancing = False

manager.onEnter(None,EnterProximity)