import viz
import vizact
import vizmat

viz.setMultiSample(4)
viz.fov(60)
viz.go()

pic = viz.addTexture('lake3.jpg')
pic.wrap(viz.WRAP_T, viz.CLAMP_TO_BORDER)
pic.wrap(viz.WRAP_S, viz.MIRROR)

quad = viz.addTexQuad()
quad.setPosition([-.75, 2, 3])
quad.texture(pic)

quad2 = viz.addTexQuad()
quad2.setPosition([.75, 2, 3])
quad2.texture(pic)

matrix = vizmat.Transform()
matrix.setScale([1.5,1.5,1])
matrix.setTrans([-.25,-.25,1])
quad2.texmat(matrix)

WALL_SCALE = [10, 3, 1]
wall = viz.addTexQuad()
wall.setPosition( [0, 2, 3] )
wall.zoffset(1)
wall.setScale( WALL_SCALE )

matrix = vizmat.Transform()
matrix.setScale( WALL_SCALE )
wall.texmat( matrix )

bricks = viz.addTexture('brick.jpg')
bricks.wrap(viz.WRAP_T, viz.REPEAT)
bricks.wrap(viz.WRAP_S, viz.REPEAT)

wall.texture(bricks)