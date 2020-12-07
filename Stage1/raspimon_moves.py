from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#colors
r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0)   #blank (black)
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

raspimon = [
k, k, d, d, d, d, k, k,
k, d, d, w, d, w, d, k,
d, d, d, k, d, k, d, d,
d, d, r, d, d, d, r, d,
p, p, d, d, k, d, d, p,
k, r, r, d, d, d, p, k,
r, r, r, r, p, p, p, p,
k, k, k, k, k, k, k, k
]       

raspimon2 =[
k, k, d, d, d, d, k, k,
k, d, d, d, d, d, d, k,
d, d, d, d, d, d, d, d,
d, d, r, d, d, d, r, d,
p, p, d, d, k, d, d, p,
k, r, r, d, d, d, p, k,
r, r, r, r, p, p, p, p,
k, k, k, k, k, k, k, k
]

sense.set_pixels(raspimon)

#Create animation below
sense.set_pixels(raspimon2)
sleep(.2)
sense.set_pixels(raspimon2)
sleep(.2)
sense.set_pixels(raspimon)
sleep(.3)
sense.set_pixels(raspimon2)
sleep(.2)
sense.set_pixels(raspimon)
sleep(.3)
sense.set_pixels(raspimon2)
sleep(.2)
sense.set_pixels(raspimon)
sleep(.3)
sense.flip_h()
sleep(.4)
sense.flip_h()
sleep(.4)
sense.flip_h()
sleep(.4)
