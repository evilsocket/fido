FIDO
==

Fido is a minimalistic C/C++ project generator supporting various templates.

Installation
==

    python setup.py build
    sudo python setup.py install

Usage
==

    Usage: fido <action> [template] (path)

    Available actions:

                    help : Print the usage menu.
                  create : Create a project with the specified template, requires a template and a path.
                   build : Build the current project.
                   clean : Clean built files for the current project.

    Available templates:

          android-make-c : Create a native Android C project based on Makefile.
        android-make-cpp : Create a native Android C++ project based on Makefile.
                 cmake-c : Create a C project based on CMake.
               cmake-cpp : Create a C++ project based on CMake.
                  make-c : Create a C project based on Makefile.
                make-cpp : Create a C++ project based on Makefile.

Example
==

![screenshot](https://github.com/evilsocket/fido/raw/master/screenshot.png)

License
==

This project is copyleft of [Simone Margaritelli](http://www.evilsocket.net/) and released under the GPL 3 license.