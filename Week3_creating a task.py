import viz
import vizact
import viztask

viz.setMultiSample(4)
viz.fov(60)
viz.go()

dojo = viz.addChild('dojo.osgb')

viz.MainView.move([0,0,-5])

male = viz.addAvatar('vcc_male.cfg')
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([-2,0,0])
female.setEuler([90,0,0])
male.setPosition([2,0,0])
male.setEuler([-90,0,0])

male.state(1)
female.state(1)

question_text = viz.addText('Hit spacebar to start', viz.SCREEN)
question_text.setScale([.4,.4,.4])
question_text.setPosition([.35,.75,0])
question_text.setBackdrop(viz.BACKDROP_OUTLINE)

def myTask():
    while True:
        question_text.message('Hit the spacebar to begin.')
        yield viztask.waitKeyDown(' ')
        female.state(5)
        yield viztask.waitTime(1)
        yield viztask.addAction( male,  vizact.walkTo([-1,0,0]))
        male.state(5)
        yield mySubTask()
        male.state(9)
        yield viztask.addAction( female, vizact.animation(6))
        male.addAction(vizact.walkTo([2,0,-1],2.5,90,11))

viztask.schedule(myTask())
def mySubTask():
    while True:
        question_text.message('Do they keep dancing? (y/n)')
        d = yield viztask.waitKeyDown(['y','n'])
        if d.key == 'n':
            question_text.message('')
            return