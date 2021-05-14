﻿import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Set up the environment and proximity sensors

dojo = viz.addChild('dojo.osgb')

#Create proximity manager and set debug on. Toggle debug with d key
manager = vizproximity.Manager()
manager.setDebug(viz.ON)
debugEventHandle = vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

def EnterSphere(e, sphere, color):
    sphere.runAction(vizact.fadeTo(color,time=1))

def ExitSphere(e, sphere):
    sphere.runAction(vizact.fadeTo(viz.WHITE,time=1))

sphereSensors = []
def AddSphere(name, color, position):

    sphere = vizshape.addSphere(radius=0.2)
    sphere.setPosition(position)

    sensor = vizproximity.addBoundingSphereSensor(sphere,scale=5)
    sensor.name = name
    sphereSensors.append(sensor)
    manager.addSensor(sensor)

    manager.onEnter(sensor, EnterSphere, sphere, color)
    manager.onExit(sensor, ExitSphere, sphere)

AddSphere('red', viz.RED, [0,1.8,4])
AddSphere('blue', viz.BLUE, [3.5,1.8,2])
AddSphere('yellow', viz.YELLOW, [3.5,1.8,-2])
AddSphere('green', viz.GREEN, [0,1.8,-4])
AddSphere('purple', viz.PURPLE, [-3.5,1.8,-2])
AddSphere('gray', viz.GRAY, [-3.5,1.8,2])

centerSensor = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(0.0,0.0)),None)
manager.addSensor(centerSensor)

info = vizinfo.InfoPanel("Explore the environment\nPress 'd' to toggle the visibility of the sensors\nPress spacebar to begin the experiment")

def participantInfo():
    pass

def learnPhase():
    pass

def testPhase():
    pass

def experiment():

    yield viztask.waitKeyDown(' ')

    participant = yield participantInfo()
    yield learnPhase()
    results = yield testPhase()

viztask.schedule(experiment)

def participantInfo():

    manager.setDebug(viz.OFF)
    debugEventHandle.setEnabled(viz.OFF)

    info.visible(viz.OFF)

    participantInfo = vizinfo.InfoPanel('',title='Participant Information',align=viz.ALIGN_CENTER, icon=False)

    textbox_last = participantInfo.addLabelItem('Last Name',viz.addTextbox())
    textbox_first = participantInfo.addLabelItem('First Name',viz.addTextbox())
    textbox_id = participantInfo.addLabelItem('ID',viz.addTextbox())
    participantInfo.addSeparator(padding=(20,20))

    radiobutton_male = participantInfo.addLabelItem('Male',viz.addRadioButton(0))
    radiobutton_female = participantInfo.addLabelItem('Female',viz.addRadioButton(0))
    droplist_age = participantInfo.addLabelItem('Age Group',viz.addDropList())
    ageList = ['20-30','31-40','41-50','51-60','61-70']
    droplist_age.addItems(ageList)
    participantInfo.addSeparator()

    submitButton = participantInfo.addItem(viz.addButtonLabel('Submit'),align=viz.ALIGN_RIGHT_CENTER)
    yield viztask.waitButtonUp(submitButton)

    data = viz.Data()
    data.lastName = textbox_last.get()
    data.firstName = textbox_first.get()
    data.id = textbox_id.get()
    data.ageGroup = ageList[droplist_age.getSelection()]

    if radiobutton_male.get() == viz.DOWN:
         data.gender = 'male'
    else:
         data.gender = 'female'

    participantInfo.remove()

    viztask.returnValue(data)

def learnPhase():

    info.setText("You'll have 30 seconds to walk around and learn the true color of each sphere")
    info.visible(viz.ON)

    yield viztask.waitTime(5)
    info.visible(viz.OFF)

    yield viztask.waitTime(30)
    info.setText("Please return to the center of the room to begin the testing phase") 
    info.visible(viz.ON)

    yield viztask.waitTime(5)

def testPhase():

    results = []
    trials = [3,2,0,4,1]

    for i in trials:

        if centerSensor not in manager.getActiveSensors():
            yield vizproximity.waitEnter(centerSensor)

        sensor = sphereSensors[i]

        instruction = 'Walk to the {} sphere'.format(sensor.name)
        info.setText(instruction)

        startTime = viz.tick()

        yield vizproximity.waitEnter(sensor)
        info.setText('Please return to the center of the room')

        elapsedTime = viz.tick() - startTime

        results.append((sensor.name, elapsedTime))

    info.setText('Thank You. You have completed the experiment')

    viztask.returnValue(results)

def experiment():

    yield viztask.waitKeyDown(' ')

    participant = yield participantInfo()
    yield learnPhase()
    results = yield testPhase()

    try:
        with open(participant.id + '_experiment_data.txt','w') as f:

            data = "Participant ID: {p.id}\nLast Name: {p.lastName}\nFirst Name: {p.firstName}\nGender: {p.gender}\nAge: {p.ageGroup}\n\n".format(p=participant)
            f.write(data)

            for name,time in results:
                data = "The {} trial took {:.2f} seconds\n".format(name,time)
                f.write(data)
    except IOError:
        viz.logWarn('Could not log results to file. Make sure you have permission to write to folder')