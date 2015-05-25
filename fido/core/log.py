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
class Log:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    @staticmethod
    def d( msg ):
        print "[D] %s" % msg

    @staticmethod
    def i( msg ):
        print (Log.BOLD + "[I] %s" + Log.ENDC) % msg

    @staticmethod
    def w( msg ):
        print (Log.WARNING + "[W] %s" + Log.ENDC) % msg

    @staticmethod
    def e( msg ):
        print (Log.ERROR + "[E] %s" + Log.ENDC) % msg

    @staticmethod
    def fatal( msg ):
        Log.e(msg)
        quit()