import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

pigeons = []
for eachnumber in range(6):
    newPigeon = viz.addAvatar('pigeon.cfg')

    newPigeon.setPosition([eachnumber, 0,5])
    pigeons.append(newPigeon)
    if eachnumber < 2:
        newPigeon.add(vizact.spin(1,0,0,90))
    elif eachnumber >= 2 and eachnumber < 4:
        newPigeon.add(vizact.spin(0,1,0,90))
    else:
        newPigeon.add(vizact.spin(0,0,1,90))

viz.MainView.move([2.5,-1.5,1])