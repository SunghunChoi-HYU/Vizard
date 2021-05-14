import viz

viz.go()

for i in range(5):
    ball = viz.add('white_ball.wrl')
    ball.setPosition(i*.2,1.8,3)
