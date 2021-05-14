cows = 4
pigs = 10
beasts = cows + pigs
chickens = "chickens"
roosters = "roosters"
print( cows)
print( pigs)
print( beasts)
print( chickens)
print( roosters)
barn = [cows, pigs, beasts]
henhouse = [chickens,roosters]
print("The array barn contains:",  barn)
print("The array henhouse contains:", henhouse)
print( cows, "=",  barn[0])
print( roosters, "=",  henhouse[1])

for bird in henhouse:
    print("A fox ate the", bird, ".")

for number in range(4):
    print("Close the barn door.")

for number in range(5):
    if cows > 1:
        print("Join us for a barbeque")
        cows = cows -1
    elif cows == 1:
        print("Last barbeque today")
        cows = cows -1
    else:
        print("No barbeque today")

def newlitter(animal):
    newnumber = animal*3
    return newnumber

new_pigs = newlitter(pigs)
new_cows = newlitter(cows)

print("The new number of pigs is", new_pigs)
print("The new number of cows is", new_cows)

print(newnumber)

def newAnimal():
    global goats
    goats = 7

newAnimal()
print(goats)

def changeVariable():
	global goats
	goats = 10

changeVariable()
print(goats)