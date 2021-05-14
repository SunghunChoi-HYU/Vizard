import viz
import math
viz.go()

viz.MainView.setPosition(0,2,0)
viz.MainView.setEuler(0,90,0)

viz.clearcolor([.3,.3,.3])

spider = viz.add('art/spider/spider1.cfg')
spider_bone = spider.getBone('bone_root')
spider.texture(viz.addTexture('art/spider/euro_cross.tif'))
spider.setScale(.04,.04,.04)
spider.state(2)

increment = 0
C = 0.01

def move_spider():
	global increment
	increment = increment + 0.005*20
	x = C*increment*math.cos( increment )
	z = C*increment*math.sin( increment )
	spider.setPosition([x,0,z])
	face_angle = vizmat.AngleToPoint([0,0], [x,z]) -90
	spider.setEuler([face_angle,0,0])
vizact.ontimer(.01,move_spider)

viz.startLayer(viz.LINE_STRIP)
viz.vertex(0,0,0)
myweb = viz.endLayer()

myweb.dynamic()
current_vertex = myweb.addVertex([0,0,0])
web_link = viz.link (spider, myweb.Vertex(0))
def lay_web():
	global web_link, current_vertex
	web_link.remove()
	myweb.setVertex(current_vertex, spider.getPosition())
	current_vertex = myweb.addVertex(spider.getPosition())
	web_link = viz.link(spider_bone, myweb.Vertex(current_vertex))
vizact.ontimer(0.5, lay_web)