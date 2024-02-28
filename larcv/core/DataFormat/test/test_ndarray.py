import ROOT,sys

k=ROOT.larcv.Image2D(20,20)
k.paint(0)
for x in range(20):
    for y in range(20):
        v=0
        if x==y: v=1
        k.set_pixel(x,y,v)
        # print(v,)
    # print()
print()

print(type(k))
j=ROOT.larcv.as_ndarray(k)

for x in range(len(j)):
    for y in range(len(j[x])):
        print(int(j[x][y]),)
    print()
print()
    
for x in range(k.meta().cols()):
    for y in range(k.meta().rows()):
        print(k.pixel(x,y),)
    print()
print()

import matplotlib.pyplot as plt

img=plt.imshow(j)
img.write_png('aho.png')
sys.stdin.readline()
