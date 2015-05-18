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
import glob
import imp
import os
import fido
import collections

class Loader:
    def __init__(self):
        self.basepath  = os.path.dirname( fido.__file__ )
        self.templates = []

        files = glob.glob( os.path.join( self.basepath, "templates/*.py" ) )
        files.sort()

        for file in files:
            if file.endswith( '__init__.py' ):
                continue

            name = os.path.basename(file).replace(".py", "")
            tpl = imp.load_source( name, file ).template_load()
            self.templates.append( ( tpl.get_name(), tpl ) )

        self.templates = collections.OrderedDict(self.templates)