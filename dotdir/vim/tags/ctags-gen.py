#! /usr/bin/env python

import sys
import os

ctags='ctags -R'

perls_tags = 'perls-tags'
perls_3rd = 'perls-3rd-party-tags'

perls_src = '~/perls/src/'
lcm_src = '~/perls/third-party/build/lcm-*'
bot_src = '~/perls/third-party/build/libbot2'
sam_src = '~/perls/third-party/build/isam-*'

if __name__ == '__main__':
    # generate perls tags
    cmd = ' '.join ([ctags,
        perls_src])
    os.system (cmd)
    os.rename ('tags', perls_tags)

    # generate perls third party tags
    cmd = ' '.join ([ctags,
        lcm_src,
        bot_src,
        sam_src])
    os.system (cmd)
    os.rename ('tags', perls_3rd)

    sys.exit (0)
