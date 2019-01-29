#replace file ext.
import glob
import os.path
files = glob.glob('*.exe')
for x in files:
    if not os.path.isdir(x):
        print (x)
        x2 = x.replace('.exe', '')
        print ('==> ' + x2)
        os.rename(x, x2)