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
import os

class CMakeC(BaseTemplate):
    def get_name(self):
        return "cmake-c"

    def get_description(self):
        return "Create a C project based on CMake."

    def do_build(self):
        if not os.path.isfile("Makefile"):
            os.system( "cmake ." )

        os.system("make")

    def do_clean(self):
        if not os.path.isfile("Makefile"):
            os.system( "cmake ." )

        os.system("make clean")

    def do_reset(self):
        if os.path.isfile("Makefile"):
            os.system("make clean")

        os.system( 'find . -name "CMakeFiles" -or -name "CMakeCache.txt" -or -name "cmake_install.cmake" -or -name "Makefile" | xargs rm -rf' )

def template_load():
    return CMakeC()
