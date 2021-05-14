import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go() 

logo = viz.addChild('logo.ive')
logo.setPosition([0,1,3])

tex1 = viz.addTexture('gb_noise.jpg')
tex2 = viz.addTexture('brick.jpg')

logo.texture(tex1)
logo.texture(tex2,'',1)

blend = viz.addFragmentProgram('multitexblend.fp')
logo.apply(blend)

blend.param(0,0)

slider = viz.addSlider()
slider.setPosition(0.5,0.1)

def blendTextures(pos):
    blend.param(0,pos)

vizact.onslider(slider, blendTextures)