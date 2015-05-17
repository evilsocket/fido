# This file is part of Fido.
#
# Copyright(c) 2015 Simone Margaritelli
# evilsocket@gmail.com
# http://www.evilsocket.net
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 2 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
import os
import shutil

class BaseTemplate(object):
    def __init__(self):
        self.mypath = os.path.realpath( os.path.join( os.path.dirname( os.path.realpath(__file__) ), '../templates/data', self.get_name() ) )

    def get_name(self):
        raise "Called get_name of base class!"

    def get_description(self):
        raise "Called get_description of base class!"

    def do_create(self, path):
        shutil.copytree( self.mypath, path )

        vars = {
            "#PROJECT_NAME#" : os.path.basename(path)
        }

        for root, dirnames, filenames in os.walk( path ):
            for fname in filenames:
                filename = os.path.join( root, fname )
                with open(filename, 'rt') as fd:
                    data = fd.read()

                for token, value in vars.iteritems():
                    if token in data:
                        print "  - Updating variable '%s' in %s ..." % ( token, filename )
                        data = data.replace( token, value )

                with open(filename, 'wt') as fd:
                    fd.write(data)

        print "[-] DONE\n"

    def do_build(self):
        raise "Called do_build of base class!"

    def do_clean(self):
        raise "Called do_clean of base class!"