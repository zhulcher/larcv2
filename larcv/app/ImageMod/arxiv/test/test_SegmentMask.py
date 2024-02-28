from larcv import larcv
import os, sys
larcv.logger.force_level(0)

#
# Constants
#
MSG_LEVEL=larcv.msg.Level_t.kERROR
if 'debug' in sys.argv:
    MSG_LEVEL = larcv.msg.Level_t.kDEBUG
if 'info' in sys.argv:
    MSG_LEVEL = larcv.msg.Level_t.kINFO

OUT_FNAME="segmask.root"
NUM_EVENT=1

ERROR_FILE_EXIST      = 1
ERROR_WRITE_INIT      = 2

if os.path.isfile(OUT_FNAME):
    print("Test output file (%s) already exists..." % OUT_FNAME)
    sys.exit(ERROR_FILE_EXIST)

from larcv import larcv
o=larcv.IOManager(larcv.IOManager.kWRITE)
o.reset()
o.set_verbosity(MSG_LEVEL)
o.set_out_file(OUT_FNAME)

p = larcv.SegmentMask()
cfg = larcv.CreatePSetFromFile(sys.argv[1],"SegmentMask")
p.configure(cfg)
p.initialize()

if not o.initialize():
    sys.exit(ERROR_WRITE_INIT)
for idx in range(NUM_EVENT):

    img = larcv.Image2D(10,10)
    for x in range(img.as_vector().size()):
        if x%2 == 0: img.set_pixel(x,larcv.kROIEminus)
        else: img.set_pixel(x,larcv.kROIGamma)
        
    event_image1 = o.get_data(larcv.kProductImage2D,"original")
    event_image1.Append(img)
    event_image2 = o.get_data(larcv.kProductImage2D,"target")
    event_image2.Append(img)

    o.set_id(0,0,idx)
    p.process(o)
    o.save_entry()

    idx+=1

p.finalize()
o.finalize()
