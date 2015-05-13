#!/usr/bin/env python
"""
This install script will create all the symlinks to the files within
the dotfiles directory as well as update vim with the lastest plugins
"""

import os
from os.path import expanduser
import shutil
import subprocess


def dofiles_install():
    """ Installs all the dotfiles and updates vim """
    home = expanduser('~')
    dotfiles = '{}/.dotfiles'.format(home)

    symlink_files = {\
                        '/.tmux': '/tmux',
                        '/.tmux.conf': '/tmux/tmux.config',
                    }

    for file_name, location in symlink_files.iteritems():
        sym_file = '{}{}'.format(home, file_name)
        source_file = '{}{}'.format(dotfiles, location)
        if os.path.islink(sym_file):
            os.remove(sym_file)
        elif os.path.isfile(sym_file):
            os.remove(sym_file)
        elif os.path.isdir(sym_file):
            shutil.rmtree(sym_file)
        else:
            print '{} doesn\'t exist'.format(sym_file)

        print 'Creating symlink {} to {}'.format(sym_file, source_file)
        os.symlink(source_file, sym_file)


if __name__ == '__main__':
    dofiles_install()