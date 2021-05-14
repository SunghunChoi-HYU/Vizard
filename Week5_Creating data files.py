import viz
import vizinput

viz.setMultiSample(4)
viz.fov(60)
viz.go()

subject = vizinput.input('What is the participant number?')

viz.move([0,0,2])

piazza = viz.addChild('piazza.osgb')

pigeon = viz.addAvatar('pigeon.cfg',pos=[-0.9, 2.88, 11.3],euler=[100,0,0])
pigeon.state(1)

critical_question = viz.addText('Do you see a pigeon?',viz.SCREEN)

yes = viz.addText('Yes!',viz.SCREEN)
no = viz.addText('No!',viz.SCREEN)

critical_question.alignment(viz.ALIGN_CENTER_TOP)
critical_question.setPosition(.5,.9)

yes.alignment(viz.ALIGN_LEFT_TOP)
yes.setPosition(.25,.75)

no.alignment(viz.ALIGN_LEFT_TOP)
no.setPosition(.75,.75)

yes_button = viz.addButton()
yes_button.setPosition(.22,.71)

no_button = viz.addButton()
no_button.setPosition(.72,.71)

start_time = viz.tick()
question_data = open('pigeon_data.txt','a')

def onbutton(obj,state):
    elapsed_time = viz.tick() - start_time
   
    if obj == yes_button:
        data = 'Subject ' + str(subject) + ' saw a pigeon.\t'
    if obj == no_button:
        data = 'Subject ' + str(subject) + ' did not see a pigeon.\t'
   
    data = data + 'Elapsed time was: ' + str(round(elapsed_time,2)) + ' seconds\n'
   
    question_data.write(data)
    question_data.flush()
    #viz.quit()

viz.callback(viz.BUTTON_EVENT,onbutton)

tracking_data = open('tracking_'+str(subject)+'.txt', 'a')

def getData():
    orientation = viz.MainView.getEuler()
    position = viz.MainView.getPosition()
    data = str(subject) + '\t' + str(orientation) + '\t' + str(position) + '\n'
    tracking_data.write(data)

vizact.ontimer(1, getData)