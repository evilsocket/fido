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
from fido.core.log import Log
import os
import shutil
import sys
import time
import re

class BaseTemplate(object):
    def __init__(self):
        self.mypath = os.path.realpath( os.path.join( os.path.dirname( os.path.realpath(__file__) ), '../templates/data', self.get_name() ) )
        self.vars   = {
            "#PROJECT_NAME#" : "",
            "#BASE_NAME#" : "",
            "#FILE_SLUG#" : "",
            "#DATE#" : time.strftime('%b %m, %Y'),
            "#USER_NAME#" : os.environ['USER']
        }

    def get_name(self):
        raise "Called get_name of base class!"

    def get_description(self):
        raise "Called get_description of base class!"

    def _update_template_data(self, filename):
        self.vars["#BASE_NAME#"] = os.path.basename(filename)
        self.vars["#FILE_SLUG#"] = re.sub( r'[^a-z0-9]+', '_', self.vars["#BASE_NAME#"] ).upper()

        with open(filename, 'rt') as fd:
            data = fd.read()

        for token, value in self.vars.iteritems():
            if token in data:
                Log.d( "  Updating variable '%s' in %s ..." % ( token, filename ) )
                data = data.replace( token, value )

        with open(filename, 'wt') as fd:
            fd.write(data)

    def do_create(self, path):
        shutil.copytree( self.mypath, path )

        Log.d( "  Creating project '.fido' file ..." )

        with open( os.path.join( path, '.fido' ), 'w+t' ) as fd:
            fd.write( "# Do not remove this file, check out FIDO at https://github.com/evilsocket/fido\n" )
            fd.write( self.get_name() )

        self.vars["#PROJECT_NAME#"] = os.path.basename(path)

        for root, dirnames, filenames in os.walk( path ):
            for fname in filenames:
                filename = os.path.join( root, fname )
                self._update_template_data(filename)

    def do_build(self):
        raise "Called do_build of base class!"

    def do_clean(self):
        raise "Called do_clean of base class!"

    def do_reset(self):
        Log.w( "Action not implemented for this template." )

    def do_add(self):
        if len(sys.argv) < 3:
            Log.fatal( "Usage: fido add <filename>( <filename> <filename> ... )" )

        for i in range(2, len(sys.argv)):
            filename  = sys.argv[i]
            name, ext = os.path.splitext( filename )
            ext = ext.lower()

            if ext in ( '.h', '.hpp' ):
                destination = 'include'

            elif ext in ( '.c', '.cpp' ):
                destination = 'src'

            else:
                destination = '.'

            filename = os.path.join( destination, filename )
            dirname  = os.path.dirname( filename )

            if os.path.isfile(filename):
                Log.fatal( "File '%s' already exists." % filename )

            Log.i( "Creating '%s' ..." % filename )

            # make sure every folder is created
            if not os.path.isdir(dirname):
                os.makedirs( dirname )

            tpl_name = os.path.join( os.path.expanduser('~'), ".fido/template%s" % ext )

            # check if a user template is available
            if os.path.isfile( tpl_name ):
                Log.i( "Using user template '%s' ..." % tpl_name )
                shutil.copy( tpl_name, filename )

                self.vars["#PROJECT_NAME#"] = os.path.basename( os.getcwd() )

                self._update_template_data(filename)

            else:
                # 'touch' it
                # add #ifdefs by default to headers
                target = open( filename, 'a')
                if ext in ( '.h', '.hpp' ):
                  target.write("#ifndef " + name.upper() + "_" + ext.upper()[1:] + "\n")
                  target.write("#define " + name.upper() + "_" + ext.upper()[1:] + "\n")
                  target.write("\n")
                  target.write("#endif")
                target.close()
