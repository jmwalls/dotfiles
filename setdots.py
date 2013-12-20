#!/usr/bin/env python
import sys 
import os

HDIR = os.getenv ('HOME')
CDIR = os.getcwd ()
DDIR = os.path.join (CDIR, 'dotdir')
ODIR = os.path.join (CDIR, 'olddir')

dots = [f for f in os.listdir (DDIR)]

def install ():
    print 'installing dot files:'
    if not os.path.exists (ODIR): os.mkdir (ODIR)
    for dot in dots:
	print '\t%s' % dot
	src = os.path.join (DDIR, dot)
	dname = ''.join (['.',dot])
	dest = os.path.join (HDIR, dname)
	if os.path.exists (dest):
            cmd = ' '.join (['mv', dest, ODIR])
            os.system (cmd)
        cmd = ' '.join (['ln -sf', src, dest])
        os.system (cmd)
    print 'installed'

def uninstall ():
    raise NotImplementedError ('need to finish uninstall logic')

def print_usage (bname):
    print 'usage: %s <install | uninstall>' % bname
    sys.exit (0)

if __name__ == '__main__':
    if len (sys.argv) < 2:
        print_usage (sys.argv[0])

    if sys.argv[1]=='install':
        install ()
    elif sys.argv[1]=='install':
        uninstall ()
    else:
        print_usage (sys.argv[0])
   
    sys.exit (0)
