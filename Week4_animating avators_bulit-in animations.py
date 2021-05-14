import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

#add the avatar and set his position and orientation
male = viz.addAvatar('vcc_male.cfg', pos=(0,0,4), euler=(180,0,0) )  

vizact.onkeydown('1', male.state, 1)
vizact.onkeydown('2', male.state, 2)
vizact.onkeydown('3', male.state, 3)  
vizact.onkeydown('4', male.speed, 2)  
vizact.onkeydown('5', male.speed, .5)  

def blendAnimations():

    male.blend(2, .5)
    male.blend(10, .5)

vizact.onkeydown('6', blendAnimations) 
vizact.onkeydown('7', male.execute, 6) 
vizact.onkeydown('8', male.stopAnimation, 2) 