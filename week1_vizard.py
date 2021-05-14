import viz
viz.go()

def inflate(who):
	inflate_animation = vizact.color(viz.Purple)
	who.addAction(inflate_animation)

balloons = []

for i in [-2, -1,0,1,2,3] :
	balloon = viz.add( 'art/balloon.ive' )
	balloon.setPosition(i,1.8,3)
	balloons.append(balloon)

inflate(balloons[2])