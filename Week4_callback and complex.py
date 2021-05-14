import viz
import vizact
import random

NUM_BALLS = 20

BUMPER_WIDTH = .2

BUMPER_DEPTH = .5

NUM_BUMPER_ROWS = 5
NUM_BUMPER_COLUMNS = 5

BUMPER_SPACING = BUMPER_WIDTH * 2

X_CENTERING_OFFSET = -(BUMPER_SPACING * NUM_BUMPER_COLUMNS) / 2

viz.setMultiSample(4)
viz.fov(60)
viz.go()

import vizinfo
vizinfo.InfoPanel(align=viz.ALIGN_LEFT_BOTTOM)

viz.MainView.setPosition( [0, 1, -2.5] )

#Turn on the physics engine
viz.phys.enable()

#Decrease the force of gravity
viz.phys.setGravity( [0, -4, 0] )

#Add backboard
backboard = viz.addTexQuad()
backboard.setScale( [2.5]*3 )
backboard.setPosition( [0, .75, .25] )
backboard.texture( viz.addTexture( 'sky_posx.jpg' ) )
backboard.collideMesh()
backboard.disable( viz.DYNAMICS ) #disable dynamic physics forces from acting on the object


#Initialize the bumpers

#Create a bumper prototype to copy for all other bumpers
bumper = viz.addChild( 'table.wrl' )
bumper.setScale( [BUMPER_WIDTH, BUMPER_DEPTH, BUMPER_WIDTH] )
#Create a collideBox for each child node rather than one encompassing the entire model
bumper.collideBox( node='Leg1', bounce = 1, friction = .00000001 )
bumper.collideBox( node='Leg2', bounce = 1, friction = .00000001 )
bumper.collideBox( node='Leg3', bounce = 1, friction = .00000001 )
bumper.collideBox( node='Leg4', bounce = 1, friction = .00000001 )
bumper.collideBox( node='Top', bounce = 1, friction = .00000001 )

bumper.getChild( 'Top' ).alpha( .2 ) #make the top of the table model transparent

bumpers = [] #list of bumpers so that we can change their colors when collided with


#Add bumpers to the world an staggered grid
isOffset = 0
xOffset = 0
y = 0
while( y < BUMPER_SPACING * NUM_BUMPER_ROWS ):

    #Stagger every other row by offseting the x cordinate
    if ( not isOffset ):
        xOffset = BUMPER_SPACING / 2
        isOffset = 1
    else:
        xOffset = 0
        isOffset = 0

    #Create a row of bumpers
    x = 0
    while( x < BUMPER_SPACING * NUM_BUMPER_COLUMNS ):

        bumperCopy = bumper.copy() #copy the master bumper object
        bumperCopy.setScale( [BUMPER_WIDTH, BUMPER_DEPTH, BUMPER_WIDTH] )
        bumperCopy.collideCopy( bumper ) #copy the physicalShape objects of the master bumper
        bumperCopy.enable( viz.COLLIDE_NOTIFY ) #We want to be notified of things colliding with the bumper
        bumperCopy.disable( viz.DYNAMICS ) #disable dynamic physics forces from acting on the object
        bumperCopy.setEuler( [0, -90, 0] )
        bumperCopy.setPosition( [x + xOffset + X_CENTERING_OFFSET, y, 0] )
        bumperCopy.runAction( vizact.spin( 0, 1, 0, 40 ) ) #spin the bumper forever
        bumpers.append( bumperCopy ) #add bumper to global list
        x += BUMPER_SPACING

    y += BUMPER_SPACING

bumper.remove() #Remove master bumper from the world


#Initialize all the balls

#Create a ball prototype to clone for all other balls
ballMaster = viz.addChild( 'beachball.osgb', pos=(0,-10,0) )
ballMaster.setScale( [BUMPER_WIDTH*1.5]*3 )
ballMaster.collideSphere( friction = .00000001, hardness = 1 )

balls = [] #list of all cloned balls

#Create clones of the master ball
for y in range(NUM_BALLS):
    ball = ballMaster.clone()
    ball.setPosition( [0, y, 0] )
    ball.setScale( [BUMPER_WIDTH*1.5]*3 )
    ball.collideCopy( ballMaster ) #Enable collisions with the ball based on a sphere shape
    balls.append( ball ) #Add the ball to the ball list

ballMaster.remove()

#Create cycle for balls
nextBall = viz.cycle( balls )

#Create object that drops the ball
ballDropper = viz.addAvatar( 'duck.cfg' )
ballDropper.setPosition( [0, 1.9, .2] )
ballDropper.setScale( [.2, .2, .2] )
ballDropper.setEuler( [180, 0, 0] )
ballDropper.state( 1 )

#Drop ball when spacebar is pressed
def dropBall():
    ball = nextBall.next() #get the next ball to drop
    ball.reset() #zero out physics forces
    ball.setPosition( ballDropper.getPosition() ) #drop ball at ballDropper's position
    ballDropper.execute( 2 )

vizact.onkeydown(' ',dropBall)

#Move ballDropper
vizact.whilekeydown(viz.KEY_UP,ballDropper.setPosition,[0,vizact.elapsed(1),0],viz.REL_PARENT)
vizact.whilekeydown(viz.KEY_DOWN,ballDropper.setPosition,[0,vizact.elapsed(-1),0],viz.REL_PARENT)
vizact.whilekeydown(viz.KEY_RIGHT,ballDropper.setPosition,[vizact.elapsed(1),0,0],viz.REL_PARENT)
vizact.whilekeydown(viz.KEY_LEFT,ballDropper.setPosition,[vizact.elapsed(-1),0,0],viz.REL_PARENT)

#Called when two objects collide in the physics simulator
def onCollide(e):
    #Did ball collide with a bumper?
    if e.obj2 in balls:
        #Change color of bumper
        e.obj1.color( random.choice( [viz.RED,viz.GREEN,viz.SKYBLUE,viz.YELLOW,viz.ORANGE,viz.PURPLE] ) )
        #Play sound at a volume appropriate for ball speed
        speed = vizmat.Vector( e.obj2.getVelocity() ).length()
        if speed > .7:
            viz.playSound( 'crashNew.wav' )
        elif speed > .4:
            viz.playSound( 'crashQuiet.wav' )
        elif speed > .1:
            viz.playSound( 'crashVeryQuiet.wav' )

viz.callback( viz.COLLIDE_BEGIN_EVENT, onCollide )

# Preload sound files
viz.playSound('crashNew.wav',viz.SOUND_PRELOAD)
viz.playSound('crashQuiet.wav',viz.SOUND_PRELOAD)
viz.playSound('crashVeryQuiet.wav',viz.SOUND_PRELOAD)