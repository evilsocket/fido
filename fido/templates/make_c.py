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

class MakeC(BaseTemplate):
    def get_name(self):
        return "make-c"

    def get_description(self):
        return "Create a C project based on Makefile."

    def do_build(self):
        os.system("make")

    def do_clean(self):
        os.system("make clean")


def template_load():
    return MakeC()
