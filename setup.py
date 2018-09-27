# This file is part of Fido
# Copyright (C) 2015 Simone 'evilsocket' Margaritelli
# evilsocket@gmail.com
# https://evilsocket.net
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from fido.version import VERSION

import os

def get_data_files():
    data = []
    for folder, subdirs, files in os.walk( 'fido/templates/data/' ):
        for fname in files:
            if fname[0] != '.':
                data.append( os.path.join( folder, fname ) )

    return data

try:
  long_description = open( 'README.md', 'rt' ).read()
except:
  long_description = 'Fido - A minimalistic C/C++ project generator.'

setup( name                 = 'fido',
       version              = VERSION,
       description          = long_description,
       long_description     = long_description,
       author               = 'Simone Margaritelli',
       author_email         = 'evilsocket@gmail.com',
       url                  = 'http://www.github.com/evilsocket/fido',
       packages             = find_packages(),
       include_package_data = True,
       package_data         = { 'fido': get_data_files() },
       scripts              = [ 'bin/fido' ],
       license              = 'GPL',
       zip_safe             = False,
       classifiers          = [
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Unix',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Programming Language :: Python',
            'Topic :: Software Development',
            'Topic :: Software Development :: Build Tools',
            'Topic :: Software Development :: Code Generators',
            'Topic :: Internet',
            'Natural Language :: English'
      ]
)
