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
class Log:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    PRINT_DEBUG_MESSAGES = False

    @staticmethod
    def d( msg ):
        if Log.PRINT_DEBUG_MESSAGES:
            print "[DEBUG] %s" % msg

    @staticmethod
    def i( msg ):
        print (Log.BOLD + "%s" + Log.ENDC) % msg

    @staticmethod
    def w( msg ):
        print (Log.WARNING + "[WARNING] %s" + Log.ENDC) % msg

    @staticmethod
    def e( msg ):
        print (Log.ERROR + "[ERROR] %s" + Log.ENDC) % msg

    @staticmethod
    def fatal( msg ):
        Log.e(msg)
        quit()
