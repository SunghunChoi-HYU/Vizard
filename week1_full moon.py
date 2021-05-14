import viz
viz.go()

viz.MainView.setPosition(0,0.68,-1.3)
model = viz.add('art/window.ive')
window = model.getChild('glass')

clouds = viz.addTexture('art/tileclouds.jpg')
moon = viz.addTexture('art/full moon.jpg')

window.texture(clouds, '',1)
window.texture(moon,'',0)

clouds.wrap(viz.WRAP_S, viz.REPEAT)
clouds.wrap(viz.WRAP_T, viz.REPEAT)

slider = viz.addSlider()
slider.setPosition(.5,.1)

def swap_textures(slider_poistion):
	cloud_amt = slider_poistion
	window.texblend(cloud_amt, '',1)

vizact.onslider(slider,swap_textures)
swap_textures(0)

matrix = vizmat.Transform()

def move_clouds():
	matrix.postTrans(.0005,.0005,0)
	window.texmat (matrix,'',1)
	
vizact.ontimer(.01,move_clouds)