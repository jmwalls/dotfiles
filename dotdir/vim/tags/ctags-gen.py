#! /usr/bin/env python

import sys
import os

ctags='ctags -R'

dngv_tags = 'dngv-tags'
perls_tags = 'perls-tags'
perls_3rd = 'perls-3rd-party-tags'

perls_src = '~/perls/src/'
dngv_src = '~/dngv/src/'

lcm_src = '~/code/third-party/lcm-1.1.2/'
bot_src = '~/code/third-party/libbot/'
sam_src = '~/perls/third-party/build/isam_dev/'

if __name__ == '__main__':
    # generate dngv tags
    cmd = ' '.join ([ctags,
        dngv_src])
    print 'executing:', cmd
    os.system (cmd)
    os.rename ('tags', dngv_tags)

    ## generate perls tags
    #cmd = ' '.join ([ctags,
    #    perls_src])
    #print 'executing:', cmd
    #os.system (cmd)
    #os.rename ('tags', perls_tags)

    # generate perls third party tags
    cmd = ' '.join ([ctags,
        lcm_src,
        bot_src,
        sam_src])
    print 'executing:', cmd
    os.system (cmd)
    os.rename ('tags', perls_3rd)

    sys.exit (0)
