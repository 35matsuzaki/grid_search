import sys

argvs = sys.argv
if len(argvs) != 2:
    print "usage python %s <read_file> " % argvs[0]
    exit()

read_file = open(argvs[1], 'r')
write_file = open(argvs[1].replace(".yaml","_writer.py"), 'w')
write_file.write("#!/usr/bin/env python\n")
write_file.write("# -*- coding: utf-8 -*-\n")
write_file.write('import sys\n')
write_file.write('import numpy as np\n')
write_file.write('argvs = sys.argv\n')
write_file.write('write_file = argvs[0].replace("_writer.py", ".yaml")\n')
write_file.write("data = np.genfromtxt('params.csv', dtype = None, delimiter=',')\n")
write_file.write('read_params = data[:,int(argvs[1])]\n')
write_file.write('file = open(write_file, "w")\n')
for line in read_file.readlines():
    write_file.write("file.write('%s')" % line.replace("\n", "\\n"))
    write_file.write("\n")

read_file.close()
write_file.close()
