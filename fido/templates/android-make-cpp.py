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

class AndroidMakeCPP(BaseTemplate):
    def _check_ndk(self):
        ndk_path = os.path.join( os.environ['HOME'], 'android/ndk' )

        if not os.path.isdir(ndk_path ):
            print ( "[!] WARNING: You don't have the NDK installed on '%s', either install it or make sure"  % ndk_path ) + \
                    "to override the environment variables ANDROID_* in your Makefile before compiling."

    def get_name(self):
        return "android-make-cpp"

    def get_description(self):
        return "Create a native Android C++ project based on Makefile."

    def do_create(self, path):
        self._check_ndk()
        super( AndroidMakeCPP, self).do_create(path)

    def do_build(self):
        self._check_ndk()
        os.system("make")

    def do_clean(self):
        self._check_ndk()
        os.system("make clean")

def template_load():
    return AndroidMakeCPP()