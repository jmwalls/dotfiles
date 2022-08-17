#!/usr/bin/env python3
"""XXX
"""
import argparse
import logging
import os
from pathlib import Path
import shutil


PATH_HOME = Path(os.getenv('HOME'))
PATH_FILE = Path(__file__).parent.resolve()


# OLDDIR = os.path.join(CURDIR, 'olddotdir')
# OLDAWEDIR = os.path.join(CURDIR, 'oldawesomedir')
#
# dots = [f for f in os.listdir(DOTDIR)]

# def install ():
#     print 'installing dot files:'
#     if not os.path.exists (OLDDIR):
#         os.mkdir (OLDDIR)
#
#     for dot in dots:
# 	print '\t%s' % dot
# 	src = os.path.join (DOTDIR, dot)
# 	dname = ''.join (['.',dot])
# 	dest = os.path.join (HOMEDIR, dname)
# 	if os.path.exists (dest):
#             shutil.move (dest, OLDDIR)
#         cmd = ' '.join (['ln -sf', src, dest])
#         os.system (cmd)
#
#     print 'installing awesome files'
#     if not os.path.exists (OLDAWEDIR): os.mkdir (OLDAWEDIR)
#     dest = os.path.join (HOMEDIR, '.config', 'awesome')
#     if os.path.exists (dest):
#         shutil.move (dest, OLDAWEDIR)
#     cmd = ' '.join (['ln -sf', AWEDIR, dest])
#     os.system (cmd)
#
#     print 'installed'


def install(*, dry_run: bool) -> None:
    """XXX
    """
    # Dot files just get installed to `~/`.
    for f in (PATH_FILE / 'dotdir').iterdir():
        dest = PATH_HOME / f'.{f.name}'
        cmd = ' '.join(['ln -sf', str(f), str(dest)])
        logging.info(f'install {cmd}')
        if not dry_run:
            os.system(cmd)

    # Awesome dir gets installed to `~/.config/awesome`.
    dest = PATH_HOME / '.config' / 'awesome'
    cmd = ' '.join(['ln -sf', str(PATH_FILE / 'awesomedir'), str(dest)])
    logging.info(f'install {cmd}')
    if not dry_run:
        os.system(cmd)


def uninstall(*, dry_run):
    """XXX
    """
    logging.info('uninstalling...')
    raise NotImplementedError('need to finish uninstall logic')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true',
                        help='print actions, but do not execute')
    parser.add_argument('--uninstall', action='store_true',
                        help='restore original dotfiles if they exist')
    args = parser.parse_args()

    if args.uninstall:
        uninstall(dry_run=args.dry_run)
    else:
        install(dry_run=args.dry_run)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')
    main()
