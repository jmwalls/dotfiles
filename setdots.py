#!/usr/bin/env python
import sys
import os
import shutil

HOMEDIR = os.getenv ('HOME')
CURDIR = os.getcwd ()
DOTDIR = os.path.join (CURDIR, 'dotdir')
OLDDIR = os.path.join (CURDIR, 'olddotdir')

AWEDIR = os.path.join (CURDIR, 'awesomedir')
OLDAWEDIR = os.path.join (CURDIR, 'oldawesomedir')

dots = [f for f in os.listdir (DOTDIR)]

def install ():
    print 'installing dot files:'
    if not os.path.exists (OLDDIR):
        os.mkdir (OLDDIR)

    for dot in dots:
	print '\t%s' % dot
	src = os.path.join (DOTDIR, dot)
	dname = ''.join (['.',dot])
	dest = os.path.join (HOMEDIR, dname)
	if os.path.exists (dest):
            shutil.move (dest, OLDDIR)
        cmd = ' '.join (['ln -sf', src, dest])
        os.system (cmd)

    print 'installing awesome files'
    if not os.path.exists (OLDAWEDIR): os.mkdir (OLDAWEDIR)
    dest = os.path.join (HOMEDIR, '.config', 'awesome')
    if os.path.exists (dest):
        shutil.move (dest, OLDAWEDIR)
    cmd = ' '.join (['ln -sf', AWEDIR, dest])
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
    elif sys.argv[1]=='uninstall':
        uninstall ()
    else:
        print_usage (sys.argv[0])

    sys.exit (0)
