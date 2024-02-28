import ROOT,sys
ROOT.larcv.load_cvutil

img=ROOT.larcv.Image2D(20,20)
img.paint(0)
for row in range(20):
    for col in range(20):
        v=0
        if row==col: v=1
        img.set_pixel(row,col,v)
        # print(v,)
    # print()
print()

print(img.meta().dump())

bb = ROOT.larcv.ImageMeta(10,10,
                          10,10,
                          int(img.meta().min_x()),
                          int(img.meta().max_y()-1))
print(bb.dump())

crop=img.crop(bb)
print(crop.meta().dump())
crop_array=ROOT.larcv.as_ndarray(crop)
print(len(crop_array),len(crop_array[0]))
print()
for row in range(crop.meta().rows()):
    for col in range(crop.meta().cols()):
        print(crop.pixel(row,col),)
    print()
print()

img.overlay(crop)
img_array=ROOT.larcv.as_ndarray(img)
print(len(img_array),len(img_array[0]))
print()
for row in range(img.meta().rows()):
    for col in range(img.meta().cols()):
        print(img.pixel(row,col),)
    print()
print()
