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
from fido.core.template import BaseTemplate
from fido.core.log import Log

import os
import sys

class AndroidMakeC(BaseTemplate):
    def _check_ndk(self):
        ndk_arg  = False
        ndk_path = os.path.join( os.environ['HOME'], 'android/ndk' )

        argc = len(sys.argv)
        for i in range(1,argc):
            arg = sys.argv[i]
            if arg == "--NDK" and i < argc - 1:
                ndk_path = sys.argv[i + 1]
                ndk_arg = True
                break

            elif arg.startswith("--NDK="):
                arg, val = arg.split("=")
                ndk_path = val.strip()
                ndk_arg = True
                break

        if not ndk_arg:
            Log.w( "WARNING: No --NDK argument detected, using default NDK path ( ~/android/ndk )." )

        if not os.path.isdir(ndk_path):
            Log.w( ( "WARNING: You don't have the NDK installed on '%s', either install it or make sure "  % ndk_path ) + \
                   "to override the environment variables ANDROID_* in your Makefile before compiling." )

        return ndk_path

    def get_name(self):
        return "android-make-c"

    def get_description(self):
        return "Create a native Android C project based on Makefile."

    def do_create(self, path):
        self.vars["#NDK_PATH#"] = self._check_ndk()
        super( AndroidMakeC, self ).do_create(path)

    def do_build(self):
        os.system("make")

    def do_clean(self):
        os.system("make clean")

def template_load():
    return AndroidMakeC()
