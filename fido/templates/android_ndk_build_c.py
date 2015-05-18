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
from fido.core.template import BaseTemplate

import os

class AndroidNdkBuildC(BaseTemplate):
    def get_name(self):
        return "android-ndk-build-c"

    def get_description(self):
        return "Create a native Android C project based on the ndk-build utility."

    def do_create(self, path):
        super( AndroidNdkBuildC, self ).do_create(path)

    def do_build(self):
        os.system("ndk-build")

    def do_clean(self):
        os.system("ndk-build clean")

    def do_reset(self):
        self.do_clean()
        os.system( 'rm -rf libs obj' )

def template_load():
    return AndroidNdkBuildC()